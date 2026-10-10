import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_weather():

    city = input(f"Enter the city name:\n")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("API_KEY")}&units=metric'

    weather_data = requests.get(request_url).json()
    # pprint(weather_data)
    print(f"\nShowing current weather for {city}:\n")
    print(f"The temperature is {weather_data['main']['temp']}°C")
    print(f"Feels like {weather_data['main']['feels_like']}°C")
    print(f"Description: {weather_data['weather'][0]['description']}\n")

if __name__ == "__main__":
    get_weather()