from datetime import datetime

import requests


def get_dict_from_openweather(city: str, token: str) -> (dict, None):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={token}')
    if response.status_code == 200:
        return get_filtered_dict(response.json())
    return None


def get_filtered_dict(data: dict) -> dict:
    return {
        'country': data.get('sys').get('country'),
        'city': data.get('name'),
        'weather': data.get('weather')[0].get('main'),
        'temp': round(data.get('main').get('temp'), 1),
        'feels_like': round(data.get('main').get('feels_like'), 1),
        'humidity': data.get('main').get('humidity'),
        'wind_speed': data.get('wind').get('speed'),
        'cloudiness': data.get('clouds').get('all'),
        'sunrise': datetime.fromtimestamp(data.get('sys').get('sunrise')).strftime("%m-%d-%Y, %H:%M"),
        'sunset': datetime.fromtimestamp(data.get('sys').get('sunset')).strftime("%m-%d-%Y, %H:%M")

    }
