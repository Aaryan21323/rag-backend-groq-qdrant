from fastapi import APIRouter
from app.schemas.chat import ChatRequest
from app.services.rag_services import run_rag
#route organizer
router=APIRouter()

@router.post("/chat")
def chat_endpoint(request:ChatRequest):
    answer=run_rag(
        session_id=request.session_id,
        question=request.message
    )
    return {"answer":answer}


