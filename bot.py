#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging.config
import logging
import subprocess

from os import path

from ext.db import Database
from ext.points import Points

from telegram.utils.helpers import escape_markdown

from telegram import InlineQueryResultArticle, ParseMode, \
        InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler

def startLogger(configfile='data/log.conf', logfile='log/beanbot.log'):
    if not path.isdir('log'):
        subprocess.call(['mkdir', '-p', 'log'])

    if not path.exists(configfile):
        print('Configuration file doesn\'t exist. Qutting.')
        exit()
    else:
        print('Configuration file exists. Loading...')
        logging.config.fileConfig(configfile)

    logger = logging.getLogger('BeanBot')
    logger.debug('Logger initialized.')

def main():
    startLogger()

    db = Database()
    db = db.connect()

    pp = Points(db)
    return

if __name__ == '__main__':
    main()