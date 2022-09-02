import requests
from django.conf import settings

from rest_framework.serializers import ValidationError


def get_weather_stats(city, days):
    base_url = 'https://api.weatherapi.com/v1/forecast.json?key'
    url = f'{base_url}={settings.WEATHER_API_KEY}&q={city}&days={days}'
    response = requests.get(url)
    response_data = response.json()
    if response.status_code != 200:
        raise ValidationError(response_data['error']['message'])
    return response_data


def get_temperature_data(city, days):
    weather_data = get_weather_stats(city, days)
    data_per_day = weather_data.get('forecast', {}).get('forecastday')
    temparature_list = []
    for day in data_per_day:
        for hourly_forecast in day.get('hour', {}):
            temparature_list.append(hourly_forecast.get('temp_c'))
            
    temparature_data = {
        "maximum": round(max(temparature_list), 2),
        "minimum": round(min(temparature_list), 2),
        "average": round(sum(temparature_list) / len(temparature_list), 2),
        "median": round(sorted(temparature_list)[len(temparature_list) // 2], 2),

    }
    return temparature_data