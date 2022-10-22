from weather import * 

currentTemp = getTempF()
currentHumidity = getHumidity()
cityName = getCityName()
weatherDesc = getWeatherDesc()
countryCode = getCountryCode()
feelsLike = getFeelsLike()

print('City Name: ' + cityName)
print('Country: ' + countryCode)
print('Weather Description: ' + str(weatherDesc))
print('Tempurature: ' + str(currentTemp) + ' F')
print('Feels Like: ' + str(feelsLike) + ' F')
print('Humidity: ' + str(currentHumidity) + '%')
