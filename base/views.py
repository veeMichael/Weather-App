from django.shortcuts import render
import requests

# Create your views here.


def home(request):

    # get the city name from the request
    city_name = request.GET.get('city')

    # if theres a city name render the template with the content

    if city_name:
        weather_data = get_weather_data(city_name)

        context = {'weather_data': weather_data}
        return render(request, 'base/home.html', context)

    # render the template without any weather data

    return render(request, 'base/home.html')


def get_weather_data(city_name):
    # get the information from the api
    # api key removed from code.
    # to get an api sign up at -> https://home.openweathermap.org and generate your own API key.
    response = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=')

    # making sure the request is successful
    if response.status_code == 200:

        # converting the json data into a python dictionary
        weather_data = response.json()

        # converting weather from kelvin to fahrenheight
        temperature_f = (weather_data['main']['temp'] - 273.15) * 9/5 + 32
        temperature_f = round(temperature_f)
        weather_data['main']['temp_f'] = temperature_f

        return weather_data
    else:
        # returns error message if unsuccesful
        return "Error getting weather data"


# search function serves to GET the api request and retreieve the data
def search(request):
    city = request.GET.get('city')
    weather_data = get_weather_data(city)
    context = {'weather_data': weather_data, 'city': city}

    # return the data
    return render(request, 'base/home.html', context)
