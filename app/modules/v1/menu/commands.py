from telebot.types import KeyboardButton, ReplyKeyboardMarkup
from core.commands import BaseCommands

class MenuCommands:
    def __init__(self):
        pass

    async def get_default_menu(self):
        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        markup.add(
            KeyboardButton("/start"),
            KeyboardButton("/help")
        )
        return markup


menu_commands = MenuCommands()
