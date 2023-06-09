import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor



from aiogram import Bot, types, Dispatcher, executor
from config import tg_bot_token

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши название города!")


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
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

        await message.reply(f"Погода в городе: {city}\nТемпература: {cur_weather} °C\n"
              f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст.\nВетер: {wind} м/с\n"
              f"Координаты города: {coord}\n"
              f"Восход солнца: {sunrise_timestamp}\nЗаход солнца: {sunset_timestamp}\n"
              )


    except:
        await message.reply("Проверьте название города")


if __name__ == '__main__':
    executor.start_polling(dp)

