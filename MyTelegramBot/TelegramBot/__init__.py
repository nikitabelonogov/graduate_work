from __future__ import print_function

import logging

import requests
from io import BytesIO

from telegram.ext import *

backend_url = None
help_message = 'Send me ur face photo and I\'ll tell u who u r.'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def help(bot, update):
    """
    Sends it to users help message.
    :param bot: bot
    :param update: update
    :return:
    """
    bot.sendMessage(chat_id=update.message.chat_id, text=help_message, parse_mode='HTML')


def hello(bot, update):
    """
    Gets the photo. Sends it to backend. Gets response. Sends it to users.
    :param bot: update
    :param update: update
    :return:
    """
    new_file = bot.getFile(update.message.photo[-1].file_id)

    response = requests.get(new_file.file_path)
    image = BytesIO(response.content)

    response = requests.post(backend_url, files={"file": image})
    bot.sendMessage(chat_id=update.message.chat_id, text=response.content)


def error(bot, update, error):
    """
    Error log.
    :param bot: bot
    :param update: update
    :param error: error
    :return:
    """
    logger.warn("Update {} caused error {}".format(update, error))


def main(token, _backend_url):
    """
    Creates and configures telegram bot.
    :param _backend_url: back end url
    :param token: telegram bot token
    :return:
    """
    global backend_url
    backend_url = _backend_url
    logger.info("BackEnd URL: {}".format(backend_url))

    updater = Updater(token)

    dispatcher = updater.dispatcher

    updater.dispatcher.add_handler(CommandHandler('start', help))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(MessageHandler(Filters.photo, hello))
    dispatcher.add_error_handler(error)

    updater.start_polling()
    logger.info("Pooling started")
    updater.idle()

