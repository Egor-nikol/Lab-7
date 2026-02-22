import requests


def get_weather(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    #https://openweathermap.org/api/one-call-3?collection=one_call_api_3.0
    params = { 
        'q': city_name,
        'appid': "27503d8d30e83df5f1f8719adb9afa0c", #API
        'units': 'metric',  # градусы по цельсию
        'lang': 'ru' # вывод погоды на русском
    }

    try:
        response = requests.get(base_url, params=params) #отправляем запрос       
        data = response.json() #парсим JSON

        #находим данные
        weather_desc = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']  # в гектопаскалях

        print(f"Погода в городе {city_name}:")
        print(f"Описание: {weather_desc.capitalize()}")
        print(f"Температура: {temp}°C")
        print(f"Влажность: {humidity}%")
        print(f"Давление: {pressure} гПа")

    except: 
        print(response.status_code)


city = "Saint Petersburg"
city = "Ulianovsk"
get_weather(city)