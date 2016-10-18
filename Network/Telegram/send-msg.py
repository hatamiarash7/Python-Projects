from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
import logging

updater = Updater(token='260306319:AAFyc6Et3OaTu-QHQQwN2wo0KvjbT7X9Wkg')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Arash")

def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

start_handler = CommandHandler('start', start)
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(unknown_handler)
updater.start_polling()
updater.idle()
