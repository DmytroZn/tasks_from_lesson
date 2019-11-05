import telebot
import config
from telebot import types
from telebot.types import (
    ReplyKeyboardMarkup, 
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
import re

from mongoengine import *

connect('info_bot')

class Infor(Document):
    first_name = StringField()
    last_name = StringField()
    phone = StringField()
    email = StringField()
    street = StringField()
    comments = StringField()




bot = telebot.TeleBot(config.TOKEN)


        
name = ''
surname = ''
phone = ''
email = ''
street = ''
comments = ''

@bot.message_handler(commands=['start'])
# @bot.message_handler(content_types=['text'])
def start(message):
    bot.send_message(message.chat.id, 'Hi, I am bot')
    bot.send_message(message.chat.id, 'I ask you some information if you do not mind.')
    bot.send_message(message.chat.id, 'What is your first name?')

    bot.register_next_step_handler(message, get_name)

def get_name(message):
    global name
    name = message.text
    len_of_name = len(name)
    counter_letters = 0
    for i in name:
        if re.findall(r'[a-z-A-Z]', i):
            counter_letters += 1
        else:
            pass
    if len_of_name == counter_letters:
        bot.send_message(message.chat.id, 'Nice')
        bot.send_message(message.chat.id, 'What is your last name?')

        bot.register_next_step_handler(message, get_surname)        
    else:
        bot.send_message(message.chat.id, 'Opps. Try again, you should use only letters')
        bot.register_next_step_handler(message, get_name)


def get_surname(message):
    global surname
    surname = message.text
    len_of_surname = len(surname)
    counter_letters = 0
    for i in surname:
        if re.findall(r'[a-z-A-Z]', i):
            counter_letters += 1
        else:
            pass
    if len_of_surname == counter_letters:
        bot.send_message(message.chat.id, 'Nice')
        bot.send_message(message.chat.id, 'What is your mobile number ?')
        bot.send_message(message.chat.id, 'Write like that form +380000000000')

        bot.register_next_step_handler(message, get_phone)        
    else:
        bot.send_message(message.chat.id, 'Opps. Try again, you should use only letters')
        bot.register_next_step_handler(message, get_surname)
    

        
   
def get_phone(message):
    global phone
    phone = message.text
    one = phone[0:4]
    two = phone[4:]
    if re.match(r'[+]380', one) and re.match(r'[0-9]{9}', two) and len(two) == 9:
        bot.send_message(message.chat.id, 'Good number')
        bot.send_message(message.chat.id, 'What is your email?')

        bot.register_next_step_handler(message, get_email)
    else:
        bot.send_message(message.chat.id, 'Try again, your number should by like +380000000000')
        bot.register_next_step_handler(message, get_phone) 

    

def get_email(message):
    global email
    email = message.text

    bot.send_message(message.chat.id, 'What is your street?')

    bot.register_next_step_handler(message, get_street)

def get_street(message):
    global street
    street = message.text

    bot.send_message(message.chat.id, 'Write some comment about something?')
    bot.register_next_step_handler(message, get_comments)

def get_comments(message):
    global comments
    comments = message.text
    Infor(first_name=name, last_name=surname, phone=phone, email=email, street=street, comments=comments).save()

    bot.send_message(message.chat.id, 'Nice answers')
    bot.send_message(message.chat.id, 'Thank you very much!')
    bot.send_message(message.chat.id, 'Good bye')




bot.polling(none_stop=True)


