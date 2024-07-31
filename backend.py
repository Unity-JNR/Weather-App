import requests

class WeatherAppBackend:
    def __init__(self, api_key):
        self.api_key = api_key
        self.standard_url = 'http://api.openweathermap.org/data/2.5/weather?'

    def get_weather_data(self, city_name):
        full_url = f"{self.standard_url}q={city_name}&appid={self.api_key}&units=metric"  # Use metric units for Celsius
        try:
            response = requests.get(full_url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Something went wrong: {err}")

    def get_weather_details(self, city_name):
        weather_data = self.get_weather_data(city_name)
        if weather_data:
            main_weather_info = weather_data['main']
            min_temp = main_weather_info['temp_min']
            max_temp = main_weather_info['temp_max']
            humidity = main_weather_info['humidity']
            weather_conditions = weather_data['weather'][0]['description']
            season = self.determine_season(max_temp)
            return {
                'city': city_name,
                'humidity': humidity,
                'min_temp': f"{min_temp:.2f}",
                'max_temp': f"{max_temp:.2f}",
                'conditions': weather_conditions,
                'season': season
            }
        return None

    def determine_season(self, temperature):
        if -2 < temperature < 20:
            return 'Winter'
        elif 21 <= temperature < 30:
            return 'Spring'
        elif 31 <= temperature < 40:
            return 'Summer'
        else:
            return 'Autumn'
