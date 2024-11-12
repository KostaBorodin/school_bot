from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton
)

from aiogram.utils.keyboard import InlineKeyboardBuilder

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Расписание 🗓'),
            KeyboardButton(text='Тех. поддержка 👨‍💻')
        ],
        [
            KeyboardButton(text='Подготовка к экзаменам 📝'),
            KeyboardButton(text='Полезные ссылочки и информация 📌')
        ],
        [
            KeyboardButton(text='Поддержать бот! 💸'),
        ]
    ], resize_keyboard=True,
    input_field_placeholder='Выберите действие из меню...'
)
