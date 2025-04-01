from weather.weather import get_weather

def display_weather(city):
    try:
        data = get_weather(city)
        print(f"\nWeather in {city.capitalize()}:")
        print(f"🌡 Temperature: {data['temperature']}°C")
        print(f"🤗 Feels like: {data['feels_like']}°C")
        print(f"💧 Humidity: {data['humidity']}%")
        print(f"💨 Wind speed: {data['wind_speed']} m/s")
        print(f"🌅 Sunrise: {data['sunrise']}")
        print(f"🌇 Sunset: {data['sunset']}")
        print(f"📝 Description: {data['description'].capitalize()}")
    except ValueError as e:
        print(f"❌ {e}")
    except ConnectionError as e:
        print(f"⚠️ {e}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    display_weather(city)
