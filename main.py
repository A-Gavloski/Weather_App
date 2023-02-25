from decouple import config

import datetime as dt
import requests


BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY= config('API_KEY')
CITY = "Toronto"


def Kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius


url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()


temp_celsius = response['main']['temp']
temp_celsius = Kelvin_to_celsius(temp_celsius)
feels_like_celsius = response['main']['feels_like']
feels_like_celsius = Kelvin_to_celsius(feels_like_celsius)
humidity = response['main']['humidity']
wind_speed = response['wind']['speed']


print(f"Temperature in {CITY}: {temp_celsius:.2f}°C")
print(f"Temperature in {CITY} feels like: {feels_like_celsius:.2f}°C")
print(f"Humidity in {CITY}: {humidity:}%")
print(f"Wind speed in {CITY}: {wind_speed:.2f}°C")