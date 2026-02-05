from fastapi import FastAPI
from app.api.ingest import router as ingest_router
from app.vectorstorage.qdrant import init_collection
from app.dbase.database import Base, engine
from app.api.chat import router as chat_router

app=FastAPI(title="RAG Backend")

Base.metadata.create_all(bind=engine)
init_collection()

app.include_router(ingest_router)#registering the ingest router
app.include_router(chat_router) #registering the chat router