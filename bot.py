#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import json
import argparse
import logging.config
import logging
import subprocess

import config

from os import path

from ext.db import Database
from ext.points import Points

from telegram.utils.helpers import escape_markdown

from telegram import InlineQueryResultArticle, ParseMode, \
        InputTextMessageContent
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def startLogger():
    if not path.isdir('log'):
        subprocess.call(['mkdir', '-p', 'log'])
    
    if args.debug:
        config.LOGGER_CONFIG['handlers']['console']['level'] = 'DEBUG'

    logging.config.dictConfig(config.LOGGER_CONFIG)

    logger = logging.getLogger(__name__)
    logger.debug('Logger initialized.')

    return logger

def startArgParse():
    parser = argparse.ArgumentParser()

    parser.add_argument('-d', '--debug', help='enable debugging features',
        action='store_true')
    parser.add_argument('-s', '--setup', help='runs the setup script',
        action='store_true')

    return parser.parse_args()

def loadPoints():
    db = Database()
    db = db.connect()

    pp = Points(db)
    pps = pp.load_pps()
    return pp

def greeter(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def handleText(bot, update):
    """Handles text messages."""
    pp = loadPoints()

    def echo(bot, update):
        """Echo the user message."""
        update.message.reply_text(update.message.text)

    def plusPlus(text):
        return re.compile('\w+[+]{2}').findall(text)

    message = update.message.text

    if message.lower().startswith('.pp '):
        ppd = message.lower()[4:]
        pp.change_record('pp', ppd)
    elif message.lower().startswith('.mm '):
        ppd = message.lower()[4:]
        pp.change_record('mm', ppd)
    elif not plusPlus(message) == []:
        keywords = plusPlus(message)
        for k in keywords:
            k = k[:-2]
            pp.change_record('pp', k)
        update.message.reply_text('plus plus')

def score(bot, update):
    """Sends the top high/low scores when the command /score is issued."""
    pp = loadPoints()
    high, low = pp.get_all_scores()
    msg = '{}\n{}'.format(high, low)
    update.message.reply_text(msg, parse_mode='html')

def error(bot, update, error):
    """Log errors caused by Updates."""
    logger = startLogger()
    logger.error('Update {} caused error {}'.format(update, error))

def main():
    with open('secrets/secrets.json') as sf:
        SECRETS = json.load(sf)

    try:
        updater = Updater(SECRETS['TELEGRAM_BOT_TOKEN'])
        logger.info('Bot loaded sucessfully.')
    except:
        logger.error('Unable to load bot.')
        exit()

    updater.dispatcher.add_handler(CommandHandler('hello', greeter))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('score', score))

    updater.dispatcher.add_handler(MessageHandler(Filters.text, handleText))

    updater.dispatcher.add_error_handler(error)

    # Commented out to test webhooks
    # updater.start_polling()

    webhookListen = '127.0.0.1'
    webhookPort = 88
    updater.start_webhook(listen=webhookListen, port=webhookPort)

    updater.idle()

if __name__ == '__main__':
    args = startArgParse()
    logger = startLogger()

    if args.setup:
        subprocess.call('./setup.py')
        exit()
    else:
        try:
            main()
        except KeyboardInterrupt:
            exit()  