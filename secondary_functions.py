def dict_to_message(dct: dict) -> str:
    return f'''Country: {dct.get('country')}
City: {dct.get('city')}\n
🌞Weather: {dct.get('weather')}
🌡Temperature: {dct.get('temp')}°C
🌡Feels like: {dct.get('feels_like')}°C
💧Humidity: {dct.get('humidity')}%
💨Wind speed: {dct.get('wind_speed')}m/s
☁️Cloudiness: {dct.get('cloudiness')}%
🌅Sunrise: {dct.get('sunrise')}
🌆Sunset: {dct.get('sunset')}'''
