from flask import Flask, request, render_template
import requests

app = Flask(__name__)

api_key = "45b01a7f6a9893cc9370a6fd91f105fb"  

@app.route('/')
def home():
    """Render home page."""
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    """Fetch and display weather forecast."""
    city = request.form['city']
    country_code = request.form['country']

   
    data = fetch_weather_data(city, country_code)

    if "weather" in data and "main" in data and "wind" in data:
        
        return render_template('weather.html', data=data)
    else:
        error_message = "Failed to fetch weather data. Please check your input and API key."
        return render_template('error.html', error_message=error_message)

def fetch_weather_data(city, country_code):
    """Fetches weather data from OpenWeatherMap API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == '__main__':
    app.run(debug=True)
