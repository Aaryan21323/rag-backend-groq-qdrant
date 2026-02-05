from pydantic import BaseModel
#data validation for the bookings
class BookingReq(BaseModel):
    name:str
    email:str
    date:str
    time:str