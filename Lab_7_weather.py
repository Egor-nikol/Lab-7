import requests
    

def get_weather(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q': city_name,
        'appid': "27503d8d30e83df5f1f8719adb9afa0c", #API
        'units': 'metric',  # градусы по ццельсию
        'lang': 'ru'        # вывод погоды на русском
    }
    
    try:
        response = requests.get(base_url, params=params)        
        # Парсим JSON-ответ
        data = response.json()
        
        # Извлекаем нужные данные
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']  # в гектопаскалях (гПа)
        weather_desc = data['weather'][0]['description']
        
        # Выводим результат
        print(f"Погода в городе {city_name}:")
        print(f"Описание: {weather_desc.capitalize()}")
        print(f"Температура: {temp}°C")
        print(f"Влажность: {humidity}%")
        print(f"Давление: {pressure} гПа")
        
    except:
        print(response.status_code)

if __name__ == "__main__":
    city = "Saint"
    get_weather(city)