from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from app.core.configuration import settings

client=QdrantClient(url=settings.QDRANT_URL)

#creates a collection once 
def init_collection():
    collections=client.get_collections().collections
    names=[c.name for c in collections]

    if settings.QDRANT_COLLECTION not in names:
        client.create_collection(
            collection_name=settings.QDRANT_COLLECTION,
            vectors_config= VectorParams(
            size=384,
            distance=Distance.COSINE
            )
        )

#function to clear the collection so that the same output is not repeated when ingesting differrent function 
def clear_collection():
    """Delete all points in the collection"""
    client.delete_collection(collection_name=settings.QDRANT_COLLECTION)
    init_collection()  