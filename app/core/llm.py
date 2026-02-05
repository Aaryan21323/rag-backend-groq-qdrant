from groq import Groq
from app.core.configuration import settings

client=Groq(api_key=settings.GROQ_API_KEY) # we get key form he .env file

#calling the llm for the reasoning, using the llama-3.1-8b-instant cause it works
def call_llm(prompt:str)-> str:
    response=client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role":"system","content":"You are a helpful assistant."},
            {"role":"user","content": prompt}
        ],
        temperature=0.2
    )
    return response.choices[0].message.content