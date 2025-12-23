# Simulated WhatsApp Webhook – Health Chatbot (FastAPI)

## Overview

This project simulates a **WhatsApp webhook handler** for a health chatbot using **FastAPI**.
It demonstrates **idempotent webhook handling**, **background processing**, **rate limiting**, and **chat context usage**, as required in the assignment.

The system accepts incoming webhook messages, processes them asynchronously, and exposes a polling API to fetch generated responses.

---

## Features Implemented

* **POST /webhook**

  * Accepts WhatsApp-like webhook payloads
  * Implements **idempotency** (duplicate message detection)
  * Implements **rate limiting** (1 message / 5 seconds per user)
  * Processes messages asynchronously using `BackgroundTasks`

* **GET /responses/{message_id}**

  * Fetches processed responses
  * Returns 404 if response is not ready

* **Mock LLM Integration**

  * Generates dummy health advice (diet, exercise, sleep)
  * Easily replaceable with OpenAI / real LLM

* **User Context Support**

  * Loads per-user context from a local JSON file (simulated)

* **Media Handling**

  * Simulates media upload and extraction

* **Tests Included**

  * Idempotency test
  * Rate limit test

---

## Project Structure

```
whatsapp_sim/
├── app/
│   ├── main.py
│   ├── core/
│   │   ├── idempotency.py
│   │   ├── rate_limit.py
│   │   └── store.py
│   ├── routes/
│   │   ├── webhook.py
│   │   └── responses.py
│   ├── services/
│   │   ├── processor.py
│   │   ├── llm.py
│   │   ├── media.py
│   │   └── context.py
│   └── models/
│       └── schemas.py
├── data/
│   └── user_context.json
├── tests/
│   ├── test_idempotency.py
│   └── test_rate_limit.py
├── pytest.ini
└── README.md
```

---

## Running the Application

### 1️. Create Virtual Environment

```bash
python -m venv .venv
activate
```

### 2️. Install Dependencies with requirements.txt file

```bash
pip install -r requirements.txt
```

### 3️. Start the Server

```bash
uvicorn app.main:app --reload --port 8080
```

Swagger UI:

```
http://127.0.0.1:8080/docs
```

---

## API Usage

### - POST `/webhook`

**Request**

```json
{
  "message_id": "001",
  "from": "user123",
  "text": "low blood sugar",
  "timestamp": "2025-12-23T09:00:00Z",
  "media": "report.pdf"
}
```

**Curl**

```bash
curl -X POST http://127.0.0.1:8080/webhook \
-H "Content-Type: application/json" \
-d '{
  "message_id": "001",
  "from": "user123",
  "text": "low blood sugar",
  "timestamp": "2025-12-23T09:00:00Z",
  "media": "report.pdf"
}'
```

**Response**

```json
{
  "status": "accepted",
  "message_id": "001"
}
```

---

### - GET `/responses/{message_id}`

**Curl**

```bash
curl http://127.0.0.1:8080/responses/001
```

**Response**

```json
{
  "reply": "LLM Generated messagee",
  "processed_at": "2025-12-23T09:01:12.123Z"
}
```

---

## Running Tests

```bash
pytest -v
```

Tests included:

* Duplicate webhook handling
* Rate limiting enforcement

---

## Design Decisions

* **In-memory storage** used for simplicity and clarity
* **BackgroundTasks** used instead of Celery to keep setup minimal
* **Mock LLM** used to focus on system design rather than model accuracy
* separation of:

  * routes
  * core logic
  * services

---

## Possible Improvements

* Replace mock LLM with OpenAI / Azure OpenAI
* Persist data using SQLite/PostgreSQL
* Add authentication
* Add async task queue (Celery / Redis)
  
---

[View Project](https://github.com/Pranathi-Chintarapu64/whatsapp-sim)
