# provide the weather forecast for the weather in berkeley

from urllib.request import urlopen
import json

def get_report():
    """
    Returns the current forecase for Berkeley right now
    """

    response = urlopen('http://api.openweathermap.org/data/2.5/weather?q=Berkeley,ca&appid=7dc34849d7e8b6fbdcb3f12454c92e88')

    rawWeatherData = response.read().decode("utf-8")
    weatherData = json.loads(rawWeatherData)

    forecast = "Brekeley, CA Forecast: " + weatherData["weather"][0]["main"]
    return forecast