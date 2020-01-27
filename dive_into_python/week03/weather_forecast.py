import pprint
import requests

API_KEY_YAN_WEATHER = '7035ccff-d7e9-4a5b-830c-a2e91209ce1e'
API_KEY_YAN_GEO = 'cf35028c-8ff4-4537-9087-942f51cf1db3'


class YandexWeatherForecast:

    @staticmethod
    def get_weather(city):
        url = f'https://api.weather.yandex.ru/v1/forecast?lon={city}'
        headers = {'X-Yandex-API-Key': API_KEY_YAN_WEATHER}
        data = requests.get(url, headers=headers).json()
        return {
            'Temperature': data['fact']['temp'],
            'Pressure': data['fact']['pressure_mm'],
            'Condition': data['fact']['condition']
        }


class YandexGeo:

    @staticmethod
    def get_coordinates(city):
        url = f'https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY_YAN_GEO}' \
              f'&format=json&geocode={city}'
        data = requests.get(url).json()
        geo_pos = data['response']['GeoObjectCollection'] \
            ['featureMember'][0]['GeoObject']['Point']['pos']
        return geo_pos.split()


class CityInfo:

    def __init__(self, city, forecast_provider=None, geo_provider=None):
        self.city = city
        self._forecast_provider = forecast_provider or YandexWeatherForecast()
        self._geo_provider = geo_provider or YandexGeo()

    def weather_forecast(self):
        weather = self._forecast_provider.get_weather(self.city)
        geo = self._geo_provider.get_coordinates(self.city)
        return geo, weather


def _main():
    city = 'Moscow'
    city_info = CityInfo(city).weather_forecast()
    print(f'City: {city}')
    print(f'Geo coordinates: {city_info[0]}')
    print(f'Weather now: {city_info[1]}')


if __name__ == '__main__':
    _main()
