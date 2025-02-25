from modules.v1.start.commands import start_commands
from telebot.types import Message

from auth.decorator import access_control
from config import settings
from telebot.async_telebot import AsyncTeleBot


bot = AsyncTeleBot(settings.telegram_bot_token)

@bot.message_handler(commands=["start", "help"])
@access_control(bot=bot, admin=True)
async def send_welcome(message: Message):
    await start_commands.handle_messages(bot, message)