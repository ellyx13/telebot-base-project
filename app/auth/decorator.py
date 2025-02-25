import functools
from typing import Any, Callable
from config import settings as app_settings
from telebot.types import Message
from telebot.async_telebot import AsyncTeleBot

class access_control:

    def __init__(cls, bot: AsyncTeleBot, admin: bool = False, public: bool = False) -> None:
        cls.bot = bot
        cls.admin = admin
        cls.public = public

    async def check_authorization(self, message: Message) -> bool:
        if message.from_user.username != app_settings.telegram_admin_username:
            return False
        return True

    def __call__(cls, function) -> Callable[..., Any]:
        @functools.wraps(function)
        async def decorated(*args, **kwargs):
            message = args[0]
            is_authorize = await cls.check_authorization(message=message)
            if is_authorize is False:
                await cls.bot.reply_to(message=message, text="You are not authorized to use this bot.")
                return
            return await function(*args, **kwargs)
        return decorated
