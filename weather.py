import requests
import json
import os

# Grabs API key from system variable and also provides base URL.
apiKey = os.environ.get('openweather_apiKey')
base_url = "https://api.openweathermap.org/data/2.5/weather?"

# Grabs user input so we know what zip code to use.
# def getZip():
#     while True:
#         zip = input('Insert zip code: ')
#         return zip

# Queries the OpenWeather API to get information on the weather for the supplied zip.
def getWeather(zipCode = 16601):
    complete_url = base_url + "zip=" + zipCode + "&appid=" + apiKey
    response = requests.get(complete_url)
    jsonOut = response.json()
    return jsonOut

# Gets the current tempurature for the zip code provided in Kelvin and converts it to Farenheit.
def getTempF():
    jsonOut = getWeather()
    main = jsonOut['main']
    currentTemp = main['temp']
    tempConversion = round((currentTemp - 273.15) * 9/5 + 32, 2)
    return tempConversion

# Gets the current feels like tempurature for the zip code provided in Kelvin and converts it to Farenheit.
def getFeelsLike():
    jsonOut = getWeather()
    main = jsonOut['main']
    currentFeelsLike = main['feels_like']
    tempFeelsLikeConversion = round((currentFeelsLike - 273.15) * 9/5 + 32, 2)
    return tempFeelsLikeConversion

# Gets the current humidity for the zip code provided in Kelvin and converts it to Farenheit.
def getHumidity():
    jsonOut = getWeather()
    main = jsonOut['main']
    currentHumidity = main['humidity']
    return currentHumidity

# Gets the City for the zip code provided in Kelvin and converts it to Farenheit.
def getCityName():
    jsonOut = getWeather()
    return jsonOut['name']

# Gets the Country for the zip code provided in Kelvin and converts it to Farenheit.
def getCountryCode():
    jsonOut = getWeather()
    sys = jsonOut['sys']
    countryCode = sys['country']
    return countryCode

# Gets the current weather description for the zip code provided in Kelvin and converts it to Farenheit.
def getWeatherDesc():
    jsonOut = getWeather()
    weather = jsonOut['weather']
    weatherDesc = weather[0]['description']
    return weatherDesc