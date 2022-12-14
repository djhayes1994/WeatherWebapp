from flask import Flask, render_template, request, abort, Response
import os
import urllib
import json

# Define app
app = Flask(__name__)

@app.route('/',)
def home():
    return render_template('home.html')

@app.route('/weather', methods=['GET'])
def get_weather():
    zipCode = request.args.get('zip')
    if zipCode is None:
        abort(400, 'Missing arguement zip code')
    data = {}
    data['zip'] = request.args.get('zip')
    data['appid'] = os.environ.get('openweather_apiKey')
    data['units'] = 'imperial'
    url_values = urllib.parse.urlencode(data)
    url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = url + url_values
    data = urllib.request.urlopen(complete_url)
    resp = Response(data)
    resp.status_code = 200
    return render_template('weather.html', title='Weather App', data=json.loads(data.read().decode('utf8')))

if __name__ == '__main__':
    app.run()


