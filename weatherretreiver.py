import os


def get_weather(city_name, config_details=None):
    import requests
    import json
    api_key = config_details["weatherkey"]  # Replace with your OpenWeatherMap API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'

    # Complete url address
    complete_url = base_url + 'appid=' + api_key + '&q=' + city_name

    # Get the response from the server
    print(1)
    response = requests.get(complete_url)
    print(2)

    # Convert response to JSON format
    print(3)
    data = response.json()
    print(4)

    if data['cod'] != '404':
        main = data['main']
        weather = data['weather'][0]

        # Temperature in Celsius
        temperature = main['temp'] - 273.15

        # Weather description
        weather_description = weather['description']

        # Format the data
        weather_data = {
            'temperature': temperature,
            'description': weather_description,
            'city': city_name
        }

        print(weather_data)
        value = json.dumps(weather_data)
        return value
    else:
        return {'error': 'City not found'}
