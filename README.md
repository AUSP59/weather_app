# 🌦 Weather App (OpenWeatherMap)

A simple and modular Python CLI app that retrieves real-time weather information using the OpenWeatherMap API.

## 🚀 Features

- Real-time weather by city name
- Temperature, humidity, wind, sunrise/sunset
- Clean architecture with separated logic and interface
- Environment-safe API key loading via `.env`

## 🛠 Requirements

- Python 3.7+
- `requests`
- `python-dotenv`

## 🔧 Installation

```bash
git clone https://github.com/yourusername/weather_app.git
cd weather_app
pip install -r requirements.txt
```

## 🔑 Setup

Create a `.env` file with your API key:

```
OPENWEATHER_API_KEY=your_api_key_here
```

## ▶️ Run

```bash
python main.py
```

## 🧠 Project Structure

```
weather_app/
├── weather/          # Logic module
│   └── weather.py
├── main.py           # CLI entry point
├── .env              # API key (not tracked by Git)
├── requirements.txt
└── README.md
```

---

Want to contribute? Fork it and send a PR! 💬
