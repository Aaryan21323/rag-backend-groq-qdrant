from app.core.embed import embed_query
from app.core.llm import call_llm
from app.vectorstorage.qdrant import client
from app.core.configuration import settings
from app.memory.redis_client import redis_client
from app.services.booking_service import extract_booking_details, save_booking

def get_chat_history(session_id: str) -> str:
    key = f"chat:{session_id}"
    messages = redis_client.lrange(key, 0, 10)
    return "\n".join([m if isinstance(m, str) else m.decode('utf-8') for m in messages])
#save memoery to remember users
def save_message(session_id: str, message: str):
    key = f"chat:{session_id}"
    redis_client.lpush(key, message)
    redis_client.ltrim(key, 0, 10)

def run_rag(session_id: str, question: str) -> str:
# for boooking the data
    book_data=extract_booking_details(question)
    if book_data:
        save_booking(book_data)
        confirmation=(
            f"Interview Booked!\n\n"
            f"Name:{book_data['name']}\n"
            f"Email:{book_data['email']}\n"
            f"Date:{book_data['date']}\n"
            f"Time:{book_data['time']}"
        )
        save_message(session_id,f"user:{question}")
        save_message(session_id,f"Assistant:{confirmation}")

#change the user text into numbers
    query_vector = embed_query(question)

    
    results = client.query_points(
        collection_name=settings.QDRANT_COLLECTION,
        query=query_vector,
        limit=5
    ).points
    #for grounding the llm
    context = "\n".join([r.payload["text"] for r in results])
#to enable multi-turn chats
    history = get_chat_history(session_id)

    prompt = f"""
Context:
{context}

Chat History:
{history}

User question:
{question}
"""
    
    answer = call_llm(prompt)

    save_message(session_id, f"User: {question}")
    save_message(session_id, f"Assistant: {answer}")

    return answer