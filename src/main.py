import telebot
import requests
from telebot.types import Message
from telebot import types
from random import randint

def read_token() -> str:
    with open("./API_token.txt", "r") as file_in:
        token = file_in.read().removesuffix("\n")
        return token

API_TOKEN = read_token()
bot = telebot.TeleBot(API_TOKEN)

def get_weather(city: str):
    response = requests.get(f'https://wttr.in/{city}?format=3')
    if response.status_code == 200:
        return response.text
    else:
        return None

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('❓Помощь❓')
    item2 = types.KeyboardButton('ℹИнформацияℹ')
    item3 = types.KeyboardButton('☀Погода☀')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def bot_nessage(message):
    if message.chat.type == 'private':
        if message.text == '❓Помощь❓':
            bot.send_message(message.chat.id, "Данный бот был написан Федоровым Виктором,\nстудентом курса ♦Python для начинающих♦\nв рамках финального проекта!\n\nЭтот бот умеет:\n\n1) Выводить погоду в нескольких городах\n(☀Погода☀)\n\n2) Может рассказать о себе\n(❓Помощь❓)\n\n3) Может вывести свой логин и юзер нейм\n(ℹИнформацияℹ / 🤖Кто ты?🤖)\n\n4) Может вывести ваш логин и юзер нейм\n(ℹИнформацияℹ / 🤨Кто я?🤨)")
        
        elif message.text == 'ℹИнформацияℹ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('🤨Кто я?🤨')
            item2 = types.KeyboardButton('🤖Кто ты?🤖')
            back = types.KeyboardButton('⏮Назад⏮')

            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'Вы во вкладке: ℹИнформацияℹ', reply_markup = markup)
        
        elif message.text == '⏮Назад⏮':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('❓Помощь❓')
            item2 = types.KeyboardButton('ℹИнформацияℹ')
            item3 = types.KeyboardButton('☀Погода☀')

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, "Вы в главном меню!", reply_markup = markup)

        elif message.text == '🤨Кто я?🤨':
            bot.send_message(message.chat.id, f"{message.from_user.full_name} {message.from_user.username}")

        elif message.text == '🤖Кто ты?🤖':
            bot.send_message(message.chat.id, f"{bot.get_me().full_name} {bot.get_me().username}")
        
        elif message.text == '☀Погода☀':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Томск')
            item2 = types.KeyboardButton('Москва')
            back = types.KeyboardButton('⏮Назад⏮')

            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'Вы во вкладке: ☀Погода☀\nВыберете город!', reply_markup = markup)
        
        elif message.text == 'Томск':
            bot.send_message(message.chat.id, get_weather('Томск'))
            bot.send_message(message.chat.id, 'Выберете город!')
        
        elif message.text == 'Москва':
            bot.send_message(message.chat.id, get_weather('Москва'))
            bot.send_message(message.chat.id, 'Выберете город!')


bot.polling(non_stop=True)