import requests
import json
import os

apiKey = os.environ.get('openweather_apiKey')
base_url = "https://api.openweathermap.org/data/2.5/weather?"

def getZip():
    while True:
        zip = input('Insert zip code: ')
        return zip

def getWeather(zipCode = getZip()):
    complete_url = base_url + "zip=" + zipCode + "&appid=" + apiKey
    response = requests.get(complete_url)
    jsonOut = response.json()
    return jsonOut

def getTempF():
    jsonOut = getWeather()
    main = jsonOut['main']
    currentTemp = main['temp']
    tempConversion = round((currentTemp - 273.15) * 9/5 + 32, 2)
    return tempConversion

def getFeelsLike():
    jsonOut = getWeather()
    main = jsonOut['main']
    currentFeelsLike= main['feels_like']
    tempFeelsLikeConversion = round((currentFeelsLike - 273.15) * 9/5 + 32, 2)
    return tempFeelsLikeConversion

def getHumidity():
    jsonOut = getWeather()
    main = jsonOut['main']
    currentHumidity = main['humidity']
    return currentHumidity

def getCityName():
    jsonOut = getWeather()
    return jsonOut['name']

def getCountryCode():
    jsonOut = getWeather()
    sys = jsonOut['sys']
    countryCode = sys['country']
    return countryCode


def getWeatherDesc():
    jsonOut = getWeather()
    weather = jsonOut['weather']
    weatherDesc = weather[0]['description']
    return weatherDesc