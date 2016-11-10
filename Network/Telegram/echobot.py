# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def command_start(bot, update):
    update.message.reply_text('Hello {}'.format(update.message.from_user.first_name))

def command_help(bot, update):
    update.message.reply_text('what can i do for you ??')

def command_echo(bot, update):
    print(update.message.text)
    #update.message.reply_text(update.message.text)

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def main():
    # Create the EventHandler
    up = Updater("260306319:AAFyc6Et3OaTu-QHQQwN2wo0KvjbT7X9Wkg")
    dp = up.dispatcher
    # commands
    dp.add_handler(CommandHandler("start", command_start))
    dp.add_handler(CommandHandler("help", command_help))
    dp.add_handler(MessageHandler([Filters.text], command_echo))
    # log all errors
    dp.add_error_handler(error)
    # Start the Bot
    up.start_polling()
    up.idle()

if __name__ == '__main__':
    main()
