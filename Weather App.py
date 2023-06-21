import requests

def get_weather(city):
    api_key = ""
    url = "https://api.openweathermap.org/data/2.5/weather"
    response = requests.get(url)
    weather_data = response.json()
    return weather_data

# Example usage
city = "Atlanta"
weather = get_weather(city)
print(weather)
