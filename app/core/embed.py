from sentence_transformers import SentenceTransformer

_model=SentenceTransformer("all-miniLM-L6-v2")

def embed_documents(texts: list[str]) -> list[list[float]]:
    return _model.encode(texts).tolist()

def embed_query(text: str) -> list[float]:
    return _model.encode(text).tolist()