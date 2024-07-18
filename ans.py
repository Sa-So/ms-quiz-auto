import requests
import json
import sys
from colorama import init, Fore, Style

API_KEY = 'bd5e378503939ddaee76f12ad7a97608'

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Parse weather data
        weather = data['weather'][0]['main']
        description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']

        # Print weather forecast with colors
        print(f"Weather in {city}:")
        print(f" - Condition: {get_weather_color(weather)}{weather}{Style.RESET_ALL} ({description})")
        print(f" - Temperature: {temperature} K")
        print(f" - Humidity: {humidity}%")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Request failed: {err}")
    except KeyError:
        print("Failed to parse weather data. Please try again later.")
    except json.JSONDecodeError:
        print("Failed to decode JSON response. Please try again later.")

def get_weather_color(weather):
    if weather.lower() == 'clear':
        return Fore.YELLOW
    elif weather.lower() == 'clouds':
        return Fore.LIGHTBLUE_EX
    elif weather.lower() == 'rain':
        return Fore.BLUE
    elif weather.lower() == 'snow':
        return Fore.WHITE
    elif weather.lower() == 'thunderstorm':
        return Fore.LIGHTMAGENTA_EX
    else:
        return Fore.RESET

if __name__ == '__main__':
    init(autoreset=True)

    if len(sys.argv) < 2:
        print("Please provide a city name as an argument.")
        sys.exit(1)

    city = ' '.join(sys.argv[1:])
    get_weather(city)
