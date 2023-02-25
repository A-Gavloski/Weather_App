from decouple import config
import datetime as dt
import requests
import re
import argparse

def main():
    '''
    An application that takes a single argument as a city name and returns the weather data for that city.
    '''         

    # Create an argument parser to get the input text from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("city", help="Provide a city you want to know the weather")

    # Parse the arguments and get the input text
    args = parser.parse_args()
    input_city = args.city
    if not is_valid_city_name(input_city):
        print("Not a valid city name, please provide a valid city name.")
        return

    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    API_KEY= config('API_KEY')
    CITY = input_city


    def Kelvin_to_celsius(kelvin):
        celsius = kelvin - 273.15
        return celsius


    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
    try:                                                
        response = requests.get(url)
        if not response.status_code == requests.codes.ok:
            raise Exception(f"status_code: {response.status_code} reason: {response.reason}")
    except Exception as e:
        print(f"API call failed: {e}")
        return
    
    response = response.json()

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



def is_valid_city_name(city_name):
    '''
    Returns true if a city name is valid or not.

        Parameters:
            city_name (str): name of a city.
            
        Returns:
            is_valid (bool): True if the city name is valid.
    '''
    # City names can contain letters, spaces, and hyphens
    if not re.match(r'^[a-zA-Z\s-]+$', city_name):
        return False

    # City names must not contain consecutive spaces or hyphens
    if re.search(r'\s{2,}|-{2,}', city_name):
        return False

    # City names must be at least 2 characters long
    if len(city_name) < 2:
        return False

    return True

if __name__ == "__main__":
    main()