from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def choose_class() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="8A", callback_data="picked_8A"),
                InlineKeyboardButton(text="8Б", callback_data="picked_8Б"),
                InlineKeyboardButton(text="8В", callback_data="picked_8В")
            ]
        ]
    )
    return ikb