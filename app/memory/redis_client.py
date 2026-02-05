import redis
from app.core.configuration import settings
#redis used to store the chat history
redis_client = redis.from_url(settings.REDIS_URL, decode_responses=True)