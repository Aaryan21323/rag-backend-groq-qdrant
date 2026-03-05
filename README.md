# RAG Backend with FastAPI, Groq, and Qdrant

## Overview

This project is a production-style backend implementing a **custom Retrieval-Augmented Generation (RAG) system** using **FastAPI**. It is designed as learning projext and follows clean architecture, modular design, and industry best practices.

The system supports:

* Document ingestion (.pdf and .txt)
* Text chunking with selectable strategies
* Vector embedding using local SentenceTransformers (free, no API cost)
* Vector storage and search using Qdrant
* Multi-turn conversational RAG (no RetrievalQAChain)
* Redis-based chat memory
* Interview booking via natural language using Groq LLM

No UI is included, and no high-level RAG frameworks (LangChain RetrievalQA, FAISS, Chroma) are used.

---

## Tech Stack

* **Backend Framework:** FastAPI
* **LLM:** Groq (LLaMA 3)
* **Embeddings:** SentenceTransformers (all-MiniLM-L6-v2)
* **Vector Database:** Qdrant
* **Chat Memory:** Redis
* **Database:** SQLite (SQLAlchemy ORM)
* **Language:** Python 3.10+

---

## Project Structure

```
rag-backend/
├── app/
│   ├── main.py
│   ├── api/
│   │   ├── ingest.py
│   │   └── chat.py
│   ├── core/
│   │   ├── config.py
│   │   ├── embeddings.py
│   │   └── llm.py
│   ├── services/
│   │   ├── rag_service.py
│   │   └── booking_service.py
│   ├── schemas/
│   │   ├── chat.py
│   │   └── booking.py
│   ├── memory/
│   │   └── redis_client.py
│   ├── db/
│   │   ├── database.py
│   │   └── models.py
│   ├── utils/
│   │   ├── pdf_loader.py
│   │   └── chunking.py
│   └── vectorstore/
│       └── qdrant.py
├── requirements.txt
└── .env
```

---

## Features

### 1. Document Ingestion API

* Upload PDF or TXT files
* Extract raw text
* Apply configurable chunking strategies
* Generate embeddings locally
* Store vectors in Qdrant
* Store metadata payloads alongside vectors

Endpoint:

```
POST /ingest
```

---

### 2. Conversational RAG API

* Custom retrieval logic (no RetrievalQAChain)
* Vector similarity search using Qdrant
* Context injection into LLM prompt
* Multi-turn conversation support using Redis
* Session-based memory handling

Endpoint:

```
POST /chat
```

---

### 3. Interview Booking via Natural Language

* Detect booking intent using Groq LLM
* Extract name, email, date, and time from user text
* Store booking details in SQLite
* Confirm booking in chat response

---

## Environment Setup

### 1. Create Virtual Environment

```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key
```

---

## Running Required Services

### Start Redis

```
redis-server
```

### Start Qdrant

```
docker run -p 6333:6333 qdrant/qdrant
```

---

## Run the Application

```
uvicorn app.main:app --reload
```

API will be available at:

```
http://localhost:8000
```

Swagger UI:

```
http://localhost:8000/docs
```

---

## Example Workflow

1. Upload a document using `/ingest`
2. Ask questions about the document using `/chat`
3. Continue the conversation with the same session ID
4. Book an interview using natural language

Example booking message:

```
I want to book an interview. My name is John Doe, email john@example.com, on June 20 at 3 PM.
```

---

## Design Principles

* No vendor lock-in for embeddings
* Explicit retrieval and prompt construction
* Clear separation of concerns
* Fully typed request/response schemas
* Easily extensible architecture

---

## Author

Built as an  backend system demonstrating practical RAG system design using modern open-source tools.

