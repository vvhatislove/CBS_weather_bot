import os
import telebot
from telebot import types
import dotenv

import consts
from secondary_functions import dict_to_message
from weather_request import get_dict_from_openweather

dotenv.load_dotenv('.env')

BOT_API_TOKEN = os.getenv('BOT_API_TOKEN')
WEATHER_API_TOKEN = os.getenv('WEATHER_API_TOKEN')

bot = telebot.TeleBot(BOT_API_TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message: types.Message):
    bot.send_message(message.chat.id, consts.BOT_ANSWERS.get('start_message'))


@bot.message_handler(commands=['help'])
def start_command(message: types.Message):
    bot.send_message(message.chat.id, consts.BOT_ANSWERS.get('help_message'))


@bot.message_handler(commands=['weather_another_city'])
def start_command(message: types.Message):
    send = bot.send_message(message.chat.id, consts.BOT_ANSWERS.get('weather_another_city_message'))
    bot.register_next_step_handler(send, weather_in_another_city)


def weather_in_another_city(message: types.Message):
    dct = get_dict_from_openweather(message.text, WEATHER_API_TOKEN)
    if dct is not None:
        bot.send_message(message.chat.id, dict_to_message(dct))
    else:
        bot.send_message(message.chat.id, consts.BOT_ANSWERS.get('city_does_not_exist'))


# weather in regional cities of Ukraine
@bot.message_handler(commands=['weather'])
def weather_command(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    for city in consts.CITIES_OF_UKRAINE:
        markup.add(types.InlineKeyboardButton(text=city, callback_data=city))
    bot.send_message(message.chat.id, consts.BOT_ANSWERS.get('weather_message'), reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback(callback: types.CallbackQuery):
    for city in consts.CITIES_OF_UKRAINE:
        if city == callback.data:
            bot.send_message(callback.message.chat.id,
                             dict_to_message(get_dict_from_openweather(city, WEATHER_API_TOKEN)))
            bot.answer_callback_query(callback.id)


bot.infinity_polling()
