from config import settings
from telebot.types import Message
from modules.v1.menu.commands import menu_commands
from core.commands import BaseCommands

class StartCommands(BaseCommands):
    def __init__(self, name):
        super().__init__(name)

    async def get_description(self):
        description = (
            "Welcome to <b>Telebot Base Project</b>!\n\n"
            "This is a base project for creating Telegram bots using Python.\n\n"
            "You can use this project to create your own bots.\n\n"
        )
        return description

    async def handle_messages(self, bot, message: Message):
        description = await start_commands.get_description()
        menu = await menu_commands.get_default_menu()
        await self.send_message(bot=bot, message=message, text=description, reply_markup=menu)

start_commands = StartCommands(name="start")
