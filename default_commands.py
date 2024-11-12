from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats


# todo Дописать свои команды в меню команд
async def set_bot_commands(bot: Bot):
    custom_commands = [
        BotCommand(command="start", description="Запуск бота 🏁"),
        BotCommand(command="hadm", description="Связь с администратором 👨‍💻"),
        BotCommand(command="ry8b", description="Расписание уроков 8Б 🗓"),
        BotCommand(command="admins", description="Админ панель (доступно только для администраторов)"),
        BotCommand(command="test_start", description="Команда для бета-тестиров (в разработке)"),

    ]

    await bot.set_my_commands(
        commands=custom_commands, scope=BotCommandScopeAllPrivateChats()
    )