#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
from telegram.ext import Updater, InlineQueryHandler

def startLogger():
    if not path.isdir('log'):
        subprocess.call(['mkdir', '-p', 'log'])
    
    logging.config.dictConfig(config.LOGGER_CONFIG)

    logger = logging.getLogger('BeanBot')
    logger.debug('Logger initialized.')

def main():
    startLogger()

    db = Database()
    db = db.connect()

    pp = Points(db)
    pps = pp.load_pps()
    return

if __name__ == '__main__':
    main()