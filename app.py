from weather import * 

# Let's fill in those variables so we can print something useful to the console. 
currentTemp = getTempF()
currentHumidity = getHumidity()
cityName = getCityName()
weatherDesc = getWeatherDesc()
countryCode = getCountryCode()
feelsLike = getFeelsLike()

# Let's print the info!
print('City Name: ' + cityName)
print('Country: ' + countryCode)
print('Weather Description: ' + str(weatherDesc))
print('Tempurature: ' + str(currentTemp) + ' F')
print('Feels Like: ' + str(feelsLike) + ' F')
print('Humidity: ' + str(currentHumidity) + '%')
