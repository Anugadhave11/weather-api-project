# Weather API Project (FastAPI)

# Overview

This is a backend API built using FastAPI that fetches real-time weather data, stores it, and provides a simple chat-based interface.

# Features

* Get live weather data from external API
* Save weather data with timestamp
* Retrieve stored data
* Simple chat endpoint (`/chat`)

# Tech Stack

* Python
* FastAPI
* Requests

# Project Structure

* main.py → API logic
* data.json → stored data

# Sample Output

```json
[
  {
    "city": "pune",
    "temperature": "34",
    "time": "2026-03-31 17:06:26"
  }
]
```

# How to Run

```bash
uvicorn main:app --reload
```

Open:
http://127.0.0.1:8000/docs

## 📈 Learning Outcome

* API development
* API integration
* Data handling
* Backend fundamentals

