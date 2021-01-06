import logging
from .bot import Bot

logging.basicConfig(level=logging.INFO)
bot: Bot = Bot()

from . import handlers
