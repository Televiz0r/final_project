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

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('help')
    item2 = types.KeyboardButton('whoami')
    item3 = types.KeyboardButton('whoayou')
    item4 = types.KeyboardButton('Рандомное число')

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def bot_nessage(message):
    if message.chat.type == 'private':
        if message.text == 'help':
            bot.send_message(message.chat.id, "❗Справочная информация...🤓")
        elif message.text == 'whoami':
            bot.send_message(message.chat.id, f"{message.from_user.full_name} {message.from_user.username}")
        elif message.text == 'whoayou':
            bot.send_message(message.chat.id, f"{bot.get_me().full_name} {bot.get_me().username}")
        elif message.text == 'Рандомное число':
            bot.send_message(message.chat.id, 'Ваше число ' + str(randint(0, 1000)))

bot.polling(non_stop=True)