#Ссылка на бота: t.me/Phone_Book_Gavrilov_bot

import telebot
from telebot import types
from random import *
import json
import requests
import config

phonebook = [["Дядя Петя", "Челябинск", "12.12.1973", "12-34-6"], ["Тётя Таня", "Сергиев Посад", "11.11.1974", "20-23-46"], ["Настя", "Санкт-Петербург", "15.05.1997", "412-24-26"], ["Харис Абдрахманович", "Таганрог", "13.01.1965", "8-800-555-35-35"]]

API_TOKEN='6594391523:AAFTGzLwGtadT87OLhQzIUlVRbMSkM5mX4A'
bot = telebot.TeleBot(API_TOKEN)

def load_all_contacts():
    with open("phonebook_TG.json", "r", encoding="utf-8") as phonebook_TG_json:
        return json.load(phonebook_TG_json)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📕 All")
    btn2 = types.KeyboardButton("✔️ Add")
    btn3 = types.KeyboardButton("🔎 Info")
    btn4 = types.KeyboardButton("📝 Edit")
    btn5 = types.KeyboardButton("❌ Remove")
    btn6 = types.KeyboardButton("👌 Save")
    btn7 = types.KeyboardButton("👋 Stop")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    bot.send_message(message.chat.id, "Welcome to your contact list!\nYou can use following commands in this bot:\n /start - to launch the bot\n /stop - to stop the bot\n /all - to show all contacts in your phone book\n /add - to add new contact\n /save - to save the progress you've achieved\n /full - to learn the contact's full information by inputing his or her name\n /remove - to remove the contact from your list\n /edit - to rewrite the contact's information\n Or just use buttons following the instruction given below 😎".format(message.from_user), reply_markup=markup)
    bot.send_photo(message.chat.id, open('instruction.jpg', 'rb'))
load_all_contacts()

@bot.message_handler(content_types=['text'])
def user_choice(message):
    if (message.text == "📕 All") or (message.text == "/all"):
        show_all(message)
    elif (message.text == "✔️ Add") or (message.text == "/add"):
        get_data(message)
    elif (message.text == "🔎 Info") or (message.text == "/full"):
        learn_about_contact(message)
    elif (message.text == "📝 Edit") or (message.text == "/edit"):
        find_contact_to_edit(message)
    elif (message.text == "❌ Remove") or (message.text == "/remove"):
        find_contact_to_remove(message)
    elif (message.text == "👌 Save") or (message.text == "/save"):
        save_contacts(message)
    elif (message.text == "👋 Stop") or (message.text == "/stop"):
        stop_message(message)

#Старая версия старта
# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, "Welcome to your contact list!")
#     bot.send_message(message.chat.id, "You can use following commands in this bot:\n /start - to launch the bot\n /stop - to stop the bot\n /all - to show all contacts in your phone book\n /add - to add new contact\n /save - to save the progress you've achieved\n /full - to learn the contact's full information by inputing his or her name\n /remove - to remove the contact from your list\n /edit - to rewrite the contact's information")
# phonebook = load_all_contacts()


@bot.message_handler(commands=['stop'])
def stop_message(message):
    bot.send_message(message.chat.id, "You closed your contact list. Bye!")

@bot.message_handler(commands=['all'])
def show_all(message):
    bot.send_message(message.chat.id, "Here is your list of contacts: ")
    for i in range(len(phonebook)):
        contact = phonebook[i]
        bot.send_message(message.chat.id, contact[0])

@bot.message_handler(commands=['add'])
def get_data(message):
    message = bot.send_message(message.chat.id, "Input name, city, birthday, and phone number of your contact by writing them in one line using ',' as separator between words:")
    bot.register_next_step_handler(message, add_data)

def add_data(message):
    text = message.text.split(",")
    name = text[0]
    city = text[1]
    birthday = text[2]
    phone = text[3]
    new_contact = [text[0], text[1], text[2], text[3]]
    phonebook.append(new_contact)
    bot.send_message(message.chat.id, 'New contact was added!')

@bot.message_handler(commands=['save'])
def save_contacts(message):
    with open("phonebook_TG.json", "w", encoding="utf-8") as phonebook_TG_json:
        phonebook_TG_json.write(json.dumps(phonebook, ensure_ascii=False)) 
    bot.send_message(message.chat.id, "Changes were saved.")

@bot.message_handler(commands=['full'])
def learn_about_contact(message):
    message = bot.send_message(message.chat.id, "Input name of the contact to learn full infomation about him or her:")
    bot.register_next_step_handler(message, find_phone)

def find_phone(message):
    contact_to_find = message.text 
    for i in range(len(phonebook)):
        contact = phonebook[i]
        if contact[0] == contact_to_find:
            bot.send_message(message.chat.id, f'Contact found: \nName:{contact[0]} \nCity:{contact[1]} \nBirthday:{contact[2]} \nPhone number:{contact[3]}')

@bot.message_handler(commands=['remove'])
def find_contact_to_remove(message):
    message = bot.send_message(message.chat.id, "Input name of the contact to remove him or her from your book:")
    bot.register_next_step_handler(message, remove_contact)

def remove_contact(message):
    contact_to_remove = message.text 
    for i in range(len(phonebook)):
        contact = phonebook[i]
        if contact[0] == contact_to_remove:
            phonebook.remove(phonebook[i])
            break
    bot.send_message(message.chat.id, 'Contact was removed from your book!')

@bot.message_handler(commands=['edit'])
def find_contact_to_edit(message):
    message = bot.send_message(message.chat.id, "Input name of the contact to edit:")
    bot.register_next_step_handler(message, find_contact_position)

def find_contact_position(message):
    contact_to_edit = message.text
    for i in range(len(phonebook)):
        contact = phonebook[i]
        if contact[0] == contact_to_edit:
            message = bot.send_message(message.chat.id, f"Current data is \nName:{contact[0]} \nCity:{contact[1]} \nBirthday:{contact[2]} \nPhone number:{contact[3]}. \nInput new data in one line separating each new word with ',':")
            phonebook.remove(phonebook[i])
            break
    bot.register_next_step_handler(message, rewrite_contact_info)

def rewrite_contact_info(message):
    text = message.text.split(",")
    name = text[0]
    city = text[1]
    birthday = text[2]
    phone = text[3]
    new_contact = [text[0], text[1], text[2], text[3]]
    phonebook.append(new_contact)
    bot.send_message(message.chat.id, "Contact's information was updated!")


bot.polling()