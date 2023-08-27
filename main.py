import telebot
import schedule
import time
import random

from data import data
from databeersort import data_beer_sort

id_channel = -1001898583411

id_channel_beer = -1001645588578

bot = telebot.TeleBot('6497484445:AAG7mnXcuvhdyM7GcaEfbkDEKBj6sesE4yA')

def send_text_messages():
    bot.send_message(id_channel, random.choice(data))

def send_text_messages_beer_sort():
    bot.send_message(id_channel_beer, random.choice(data_beer_sort))

schedule.every().day.at("10:00").do(send_text_messages)
schedule.every().day.at("10:30").do(send_text_messages_beer_sort)


schedule.every().day.at("11:00").do(send_text_messages)


schedule.every().day.at("12:00").do(send_text_messages)


schedule.every().day.at("13:00").do(send_text_messages)


schedule.every().day.at("14:00").do(send_text_messages)


schedule.every().day.at("15:00").do(send_text_messages)


schedule.every().day.at("16:00").do(send_text_messages)


schedule.every().day.at("17:00").do(send_text_messages)


schedule.every().day.at("18:00").do(send_text_messages)


schedule.every().day.at("19:00").do(send_text_messages)


schedule.every().day.at("20:00").do(send_text_messages)


schedule.every().day.at("21:00").do(send_text_messages)



# Бесконечный цикл для проверки расписания
while True:
    schedule.run_pending()
    time.sleep(30)