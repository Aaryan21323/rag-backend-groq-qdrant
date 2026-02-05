from pydantic import BaseModel
#data validation for the ingest response
class IngestResponse(BaseModel):
    filename=str
    chunks_stored:int
    strat=str