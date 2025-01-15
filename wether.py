import requests
import json

# Example API endpoint for real-time weather data
weather_api_url = "https://api.weather.com/v3/weather/forecast"

# Function to fetch real-time weather data
def get_weather_data(api_key, location):
    params = {
        "apiKey": api_key,
        "location": location,
        "format": "json"
    }
    response = requests.get(weather_api_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Example usage
api_key = "06541868527a4268b2097e071ed606fb"
location = "New York, NY"
weather_data = get_weather_data(api_key, location)
if weather_data:
    print(json.dumps(weather_data, indent=2))
else:
    print("Failed to fetch weather data")
