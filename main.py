import asyncio
import os
import dotenv
import logging
import sys
import sqlite3 as sq

import keyboard as kb
from SQL import *
from schedule import *
from inline_keyboard import *

from aiogram import Dispatcher, Bot, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")
ADMIN = os.getenv("ADMIN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

class Reg(StatesGroup):
    clas_user = State()
    complaints_user = State()

# здесь происходить ответ на команду /start
@dp.message(CommandStart())
async def reg_one(message: Message):
    await message.answer(text='Добро пожаловать в чат бот Botintegral, буду рад вам помочь, но для начала должен вас придупредить что используя бота вы даёте согласие на использвание и хранения ваших данных (под данными имеется в виду имя и фамилия которые указаны в боте, а также ваш ID телеграмма', reply_markup=kb.main_kb)
                        #    text=f'В Botintegral зашел новый пользователь \n {message.from_user.full_name}'
                        #         f'\nID: {message.from_user.id}')
#   await state.set_state(Reg.clas_user)
    await add_user(message.from_user.full_name, message.from_user.id, "8Б")
    await bot.send_message(chat_id=ADMIN,
                           text=f'В Botintegral зашел новый пользователь \n {message.from_user.full_name}'
                           f'\nID: {message.from_user.id}')


@dp.message(Command('hadm'))
async def cmd_help(message: Message, state: FSMContext):
    await state.set_state(Reg.complaints_user)
    await message.answer(text='Опишите пожалуйся ваш вопрос и администрация бота в скором времени вам ответит')
 #   cursor.execute('INSERT INTO  (username, tg_id, clas) VALUES (?, ?, ?)', (user_name, user_id, '8Б'))


@dp.message(Reg.complaints_user)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(complaints_user=message.text)
    data = await state.get_data()
    await complaints_user()
#    c message.from_user.id, f'{data["complaints_user"]}'))
    await complaints_user(message.from_user.full_name, message.from_user.id, data["complaints_user"])
    await message.answer(f'Ваш вопрос отправлен администратору \n'
                         f'Ваш Вопрос: {data["complaints_user"]}')
    await state.clear()

'''
@dp.message(F.photo)
async def cmd(message: Message):
    photo_id = message.photo[-1].file_id
    await message.reply(f'{photo_id}')
'''

@dp.message(F.text.lower() == 'расписание 🗓')
async def cmd_sta(message: Message):
    await message.answer_photo(photo=FSInputFile("image/schedule.jpg"),
                               caption="Выберите свой класс ниже: ",
                               reply_markup=choose_class())
        # await message.answer(RASP_8B)


@dp.callback_query(F.data == "picked_8B")
async def push_schedule_8B(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(RASP_8B, reply_markup=choose_class_back())
    await callback.answer("Вы выбрали 8Б")


@dp.callback_query(F.data == "picked_8A")
async def push_schedule_8A(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(RASP_8A, reply_markup=choose_class_back())
    await callback.answer("Вы выбрали 8A")


@dp.callback_query(F.data == "picked_back")
async def picked_back_8B(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Выберите свой класс ниже: ", reply_markup=choose_class())
    await callback.answer("Возвращаю вас на предыдущее окно")


# дальше декраторы обрабатывают сообщение без заготовленых ответов
@dp.callback_query(F.data)
async def all_callback(callback: CallbackQuery):
    await callback.answer('Извините, но эта кнопка на этапе разработки')


@dp.message(F.text)
async def all_text(message: Message):
    await message.delete()
    await message.answer('Я точно знал ответ на ваше сообщение, но забыл, давайте сделаем вид что вы нечего не отпрвляли')


@dp.message(Command)
async def cmd_all(message: Message):
    await message.delete()
    await message.answer(text='Интересная команда, но на неё я не знаю ответа, давайте сделаем вид что вы нечего не отпрвляли')


async def main():
    await db_start()
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")