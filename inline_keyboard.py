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


def choose_class_start() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="7A", callback_data="picked_start_7A"),
                InlineKeyboardButton(text="7Б", callback_data="picked_start_7B"),
                InlineKeyboardButton(text="8А", callback_data="picked_start_8A")
            ],
            [
                InlineKeyboardButton(text="8Б", callback_data="picked_start_8B"),
                InlineKeyboardButton(text="9А", callback_data="picked_start_9A"),
                InlineKeyboardButton(text="9Б", callback_data="picked_start_9B")
            ],
            [
                InlineKeyboardButton(text="10", callback_data="picked_start_10"),
                InlineKeyboardButton(text="11", callback_data="picked_start_11")
            ]
        ]
    )
    return ikb


def exams() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="ВПР", callback_data="vpr_all"),
                InlineKeyboardButton(text="ОГЭ", callback_data="oge_all"),
                InlineKeyboardButton(text="ЕГЭ", callback_data="ege_all")
            ],
            [
                InlineKeyboardButton(text="Зачёты 7 класс", callback_data="offset_7")
            ],
            [
                InlineKeyboardButton(text="Зачёты 8 класс", callback_data="offset_8")
            ],
            [
                InlineKeyboardButton(text="Зачёт 10 класс", callback_data="offset_9")
            ]
        ]
    )
    return ikb


def links() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Сайт лицея", url='https://integral-lyceum.ru/')
            ],
            [
                InlineKeyboardButton(text="Электронный дневник", url='https://school.nso.ru/authorize')
            ],
            [
                InlineKeyboardButton(text="Ознакомиться с ботом", url='https://botintegral.tilda.ws/')
            ],
            [
                InlineKeyboardButton(text="ВПР класс", url='https://vprklass.ru/')
            ],
            [
                InlineKeyboardButton(text="Решу ОГЭ", url='https://oge.sdamgia.ru/')
            ],
            [
                InlineKeyboardButton(text="Решу ЕГЭ", url='https://ege.sdamgia.ru/')
            ],
            [
                InlineKeyboardButton(text="Подготовка к ЕГЭ по информатике", url='https://t.me/informatika_kege_itpy')
            ],
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


def cmd_help_otvet_kb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Ответить ✅", callback_data="cmd_help_otvet")
            ]

        ]
    )
    return ikb


def adm_panele() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Ответить на вопросы ✅", callback_data="cmd_help_otvet")
            ]

        ]
    )
    return ikb

