from fastapi import FastAPI
import requests
import json
from datetime import datetime

app = FastAPI()

# Home API
@app.get("/")
def home():
    return {"message": "API is working"}


# Weather function
def get_weather(city: str):
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Failed to fetch weather"}

    data = response.json()

    return {
        "city": city,
        "temperature": data["current_condition"][0]["temp_C"],
        "weather": data["current_condition"][0]["weatherDesc"][0]["value"]
    }


# Weather API
@app.get("/weather/{city}")
def weather(city: str):
    return get_weather(city)


# Save API (with timestamp)
@app.get("/save/{city}")
def save_data(city: str):
    weather = get_weather(city)

    data = {
        "city": city,
        "temperature": weather["temperature"],
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    with open("data.json", "a") as f:
        f.write(json.dumps(data) + "\n")

    return {"message": "Saved successfully", "data": data}


# Read Data API (clean JSON)
@app.get("/data")
def read_data():
    with open("data.json", "r") as f:
        return [json.loads(line) for line in f]


# Chat API (simple AI-like feature)
@app.get("/chat")
def chat(message: str):
    message = message.lower()

    if "weather" in message:
        city = message.split()[-1]
        return get_weather(city)

    return {"response": "I can tell weather. Try: weather pune"}