from __future__ import print_function

import logging

import cv2
from telegram.ext import *

from MyClassificator import MyClassificator
from MyOpenFace import MyOpenFace


def help(bot, update):
    """

    :param bot: bot
    :param update: update
    :return:
    """
    bot.sendMessage(chat_id=update.message.chat_id, text=help_message, parse_mode='HTML')


def hello(bot, update):
    """

    :param bot:
    :param update:
    :return:
    """
    new_file = bot.getFile(update.message.photo[-1].file_id)
    new_file.download(new_file.file_id)
    image = cv2.imread(new_file.file_id)
    aligned_face = openFace.face_align(image)
    if aligned_face is None:
        bot.sendMessage(chat_id=update.message.chat_id, text='Face is not found.')
    else:
        rep = openFace.forward(aligned_face)
        cv2.imwrite(new_file.file_id + '_marked.jpg', aligned_face)
        bot.sendPhoto(chat_id=update.message.chat_id, photo=open(new_file.file_id + '_marked.jpg', 'rb'))
        message = '\n'.join([str(clf.gender.predict([rep])[0])])
        bot.sendMessage(chat_id=update.message.chat_id, text=message)


def error(bot, update, error):
    """

    :param bot:
    :param update:
    :param error:
    :return:
    """
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main(token):
    """

    :param token:
    :return:
    """
    updater = Updater(token)

    dispatcher = updater.dispatcher

    updater.dispatcher.add_handler(CommandHandler('start', help))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(MessageHandler(Filters.photo, hello))
    dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()


def init(dlib_path, network_model, data_path):
    """

    :param dlib_path:
    :param network_model:
    :param data_path:
    :return:
    """
    global openFace
    global clf
    openFace = MyOpenFace(dlib_path, network_model)
    clf = MyClassificator(data_path)


help_message = 'Send me ur face photo and I\'ll tell u who u r.'
openFace = None
clf = None

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
