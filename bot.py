#!/usr/bin/env python3
# -*- coding: urt-8 -*-

from telegram.utils.helpers import escape_markdown

from telegram import InlineQueryResultArticle, ParseMode, \
        InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHelper
import logging

# Enable logging
logging.basicConfig(format='[%(asctime)s] - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)