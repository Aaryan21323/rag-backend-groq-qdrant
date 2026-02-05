from pydantic import BaseModel
#data validation for the chat
class ChatRequest(BaseModel):
    session_id: str
    message: str