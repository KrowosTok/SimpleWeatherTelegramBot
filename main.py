import requests
import datetime
from pprint import pprint 
from config import open_weather_token

def get_weather(city, open_weather_token):
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        # pprint(data)
        
        
        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"] / 1.3
        coord = data["coord"]
        wind = data["wind"]["speed"]
        cur_weather = data["main"]["temp"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        
        print(f"Погода в городе: {city}\nТемпература: {cur_weather} °C\n"
              f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст.\nВетер: {wind} м/с\n"
              f"Координаты города: {coord}\n"
              f"Восход солнца: {sunrise_timestamp}\nЗаход солнца: {sunset_timestamp}\n"
              )
        
        
    except Exception as ex:
        print(ex)
        print("Проверьте название города")

def main():
    city = input("Введите ваш город, для получения сводки: ")
    get_weather(city, open_weather_token)

if __name__ == "__main__":
    main()
