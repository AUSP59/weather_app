import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def format_weather_data(data):
    return {
        "temperature": data['main']['temp'],
        "feels_like": data['main']['feels_like'],
        "humidity": data['main']['humidity'],
        "description": data['weather'][0]['description'],
        "wind_speed": data['wind']['speed'],
        "sunrise": datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S'),
        "sunset": datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')
    }

def get_weather(city):
    if not API_KEY:
        raise ValueError("API key is missing. Please set OPENWEATHER_API_KEY in a .env file.")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=en"
    response = requests.get(url)

    if response.status_code == 200:
        return format_weather_data(response.json())
    elif response.status_code == 404:
        raise ValueError("City not found. Please check the name and try again.")
    else:
        raise ConnectionError(f"Error {response.status_code}: {response.reason}")
