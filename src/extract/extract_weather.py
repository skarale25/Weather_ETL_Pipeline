import os
import requests
import json

def extract_weather_data(api_key, location):
    """ 
    Extract weather data from OpenWeatherMap API for a given location.
    API used here provides current weather data for cities worldwide.
    """
    
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to retrieve weather data"}
