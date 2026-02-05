from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    GROQ_API_KEY: str
    QDRANT_COLLECTION: str
    QDRANT_URL: str  
    DATABASE_URL: str
    REDIS_URL:str

    model_config = SettingsConfigDict(
        env_file=str(Path(__file__).resolve().parent.parent.parent / ".env"),
        env_file_encoding='utf-8',
        case_sensitive=True
    )

# it is a singleton config oject 
settings = Settings()