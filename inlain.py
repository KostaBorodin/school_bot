from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

cmd_start_one = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='7А', callback_data='clas_db_7A'),
                InlineKeyboardButton(text='7Б', callback_data='clas_db_7B'),
                InlineKeyboardButton(text='8А', callback_data='clas_db_8A')
            ],
            [
                InlineKeyboardButton(text='8Б', callback_data='clas_db_8B'),
                InlineKeyboardButton(text='9А', callback_data='clas_db_9A'),
                InlineKeyboardButton(text='9Б', callback_data='clas_db_9B')
            ],
            [
                InlineKeyboardButton(text='10', callback_data='clas_db_10'),
                InlineKeyboardButton(text='11', callback_data='clas_db_11')
            ]
        ]
    )
