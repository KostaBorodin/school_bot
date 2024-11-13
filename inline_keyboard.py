from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def choose_class() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="7A", callback_data="picked_7A"),
                InlineKeyboardButton(text="7Б", callback_data="picked_7B"),
                InlineKeyboardButton(text="8А", callback_data="picked_8A")
            ],
            [
                InlineKeyboardButton(text="8Б", callback_data="picked_8B"),
                InlineKeyboardButton(text="9А", callback_data="picked_9A"),
                InlineKeyboardButton(text="9Б", callback_data="picked_9B")
            ],
            [
                InlineKeyboardButton(text="10", callback_data="picked_10"),
                InlineKeyboardButton(text="11", callback_data="picked_11")
            ]
        ]
    )
    return ikb


def choose_class_back() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="◀️ Назад", callback_data="picked_back")
            ]

        ]
    )
    return ikb

