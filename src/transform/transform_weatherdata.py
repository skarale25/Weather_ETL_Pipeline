from datetime import datetime

def transform_weather_data(weather_raw_data):
    """
    Transform raw weather data into a structured format.
    Converts temperature from Kelvin to Celsius and extracts relevant fields.
    """
    
    weather_data = {
        'city': weather_raw_data['name'],
        'country': weather_raw_data['sys']['country'],
        'latitude': weather_raw_data['coord']['lat'],
        'longitude': weather_raw_data['coord']['lon'],
        'weather_condition': weather_raw_data['weather'][0]['main'],
        'weather_description': weather_raw_data['weather'][0]['description'],
        'temperature_celsius': round(weather_raw_data['main']['temp'] - 273.15, 2),
        'feels_like_temp_celsius': round(weather_raw_data['main']['feels_like'] - 273.15, 2),
        'humidity_percent': weather_raw_data['main']['humidity'],
        'pressure_hpa': weather_raw_data['main']['pressure'],
        'wind_speed_mps': weather_raw_data['wind']['speed'],
        'timestamp_utc': datetime.fromtimestamp(weather_raw_data['dt']) #by default this will return timestamp in system local timezone 
    }
    
    return weather_data
    
    