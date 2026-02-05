import uuid
from fastapi import APIRouter, UploadFile, File, Query
from app.utils.pdf_load import extracttxt
from app.utils.chunking import fixed_chunk, paragraph_chunk
from app.core.embed import embed_documents
from app.vectorstorage.qdrant import client, clear_collection
from app.core.configuration import settings
from app.dbase.database import SessionLocal
from app.dbase.models import Documents

router = APIRouter()


@router.post("/ingest")
async def ingest_doc(
    file: UploadFile = File(...),
    strategy: str = Query("fixed", enum=["fixed", "paragraph"])
):
    
    clear_collection() #clear the collection before use
    
    txt = extracttxt(file) #extract the text
#choosing the chunking strat
    if strategy == "fixed":
        chunks = fixed_chunk(txt)
    else:
        chunks = paragraph_chunk(txt)

    vectors = embed_documents(chunks)

    dbase = SessionLocal()
    try:
        for vector, chunk in zip(vectors, chunks):
            client.upsert(
                collection_name=settings.QDRANT_COLLECTION,
                points=[{
                    "id": str(uuid.uuid4()),
                    "vector": vector,
                    "payload": {"text": chunk}
                }]
            )

        dbase.add(Documents(
            filename=file.filename,
            chunk_strategy=strategy,
            chunks=len(chunks)
        ))
        dbase.commit()

    except Exception as e:
        dbase.rollback()
        raise e

    finally:
        dbase.close()

    return {
        "filename": file.filename,
        "chunks_stored": len(chunks),
        "strategy": strategy
    }