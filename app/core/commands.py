from telebot.async_telebot import AsyncTeleBot
from config import settings as app_settings
from telebot.types import Message
from loguru import logger

class BaseCommands:
    def __init__(self, name: str):
        self.name = name

    async def send_message(self, bot: AsyncTeleBot, message: Message, text: str, reply_markup=None):
        try:
            await bot.reply_to(message=message, text=text, reply_markup=reply_markup, parse_mode=app_settings.parse_mode)
        except Exception as e:
            logger.error(f"Can't reply to message: {e}")