#!/usr/bin/env python3
# -*- coding: urt-8 -*-

from ext import Database, Points

from telegram.utils.helpers import escape_markdown

from telegram import InlineQueryResultArticle, ParseMode, \
        InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHelper
import logging

# Enable logging
logging.basicConfig(format='[%(asctime)s] - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)

def main():
    return
    
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.critical(f"Something went terribly wrong:\n\t{e}")