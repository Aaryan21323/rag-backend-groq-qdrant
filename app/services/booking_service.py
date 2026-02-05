import json
from app.core.llm import call_llm
from app.dbase.database import SessionLocal
from app.dbase.models import Booking
#forces llm to return only json
BOOKING_PROMPT = """
Extract interview booking details from the text.
Return ONLY valid JSON in this format:

{
"name":"",
"email":"",
"date":"",
"time":""
}

If any field is missing, use null.

Text:
"""

def extract_booking_details(text: str) -> dict | None:
    response = call_llm(BOOKING_PROMPT + text)

    try:
        data = json.loads(response)#convert the llm output to the py dict
        if all(data.get(k) for k in ["name", "email", "date", "time"]): #validation checking
            return data
    except Exception:
        return None
    
    return None

#saves the data into the database
def save_booking(data: dict):
    db = SessionLocal()
    booking = Booking(
        name=data["name"],
        email=data["email"],  
        date=data["date"],    
        time=data["time"]
    )
    db.add(booking)
    db.commit()
    db.close()

