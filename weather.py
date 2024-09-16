import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()
api_key = os.getenv('API_KEY')

@dataclass
class WeatherData:
    main: str
    # descripton: str
    # icon: str
    temperature: float

def get_lat_lon(city_name,  API_key):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},&appid={API_key}').json()
    data = response[0]
    lat,lon = data.get('lat') , data.get('lon')
    return lat,lon
    
def get_cur_weather(lat, lon,  API_key):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()
    
    data= WeatherData(
        main=response.get('weather')[0].get('main'),
        # descripton=response.get('weather')[0].get('descripton'),
        # icon=response.get('weather')[0].get('icon'),
        temperature=response.get('main').get('temp')
    )
    
    return data

def main(city_name):
    lat, lon = get_lat_lon('Bengaluru',api_key)
    Weather_data= get_cur_weather(lat,lon,api_key)
    return WeatherData
    
if __name__ == "__main__":
    lat, lon = get_lat_lon('Delhi', api_key)
    print(get_cur_weather(lat,lon,api_key))