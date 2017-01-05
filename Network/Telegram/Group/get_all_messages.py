# -*- coding: utf-8 -*-
import logging

from telegram.ext import Updater, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def command_echo(bot, update):
    print(update.message.from_user.first_name),
    print(update.message.from_user.last_name),
    print(' : '),
    print(update.message.text)


def main():
    up = Updater("260306319:AAFyc6Et3OaTu-QHQQwN2wo0KvjbT7X9Wkg")
    dp = up.dispatcher
    dp.add_handler(MessageHandler(Filters.text, command_echo))
    up.start_polling()
    up.idle()


if __name__ == '__main__':
    main()
