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
import default_commands as def_com

from aiogram import Dispatcher, Bot, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types.input_file import FSInputFile

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")
ADMIN = os.getenv("ADMIN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


class Reg(StatesGroup):
    clas_user = State()
    complaints_user = State()
    cmd_help_otvet_state = State()


# здесь происходить ответ на команду /start
@dp.message(CommandStart())
async def reg_one(message: Message, state: FSMContext):
    start_user = message.answer(text='Добро пожаловать в чат бот Botintegral, буду рад вам помочь, но для начала должен вас придупредить что используя бота вы даёте согласие на использвание и хранения ваших данных (под данными имеется в виду имя и фамилия которые указаны в боте, а также ваш ID телеграмма', reply_markup=kb.main_kb)
    start_new_user = message.answer('Выберете свой класс', reply_markup=choose_class_start())
    admin_new_user = bot.send_message(chat_id=ADMIN,
                                      text=f'В Botintegral зашел новый пользователь \n {message.from_user.full_name}'
                                           f'\nID: {message.from_user.id}')
    hello_user = message.answer('Рад снова увидеть вас!', reply_markup=kb.main_kb())
    await add_user_start(message.from_user.full_name, message.from_user.id, clas=start_new_user, clas_1=start_user, hello_user=hello_user, admin_new_user=admin_new_user)


@dp.callback_query(F.data == "picked_start_7A")
async def push_new_user_7A(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(NEW_USER_HELLO, reply_markup=kb.main_kb)
    await callback.answer("Вы выбрали 7А")
    await add_user(username=callback.from_user.full_name, tg_id=callback.from_user.id, clas='7А')


@dp.callback_query(F.data == "picked_start_7B")
async def push_new_user_7A(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(NEW_USER_HELLO, reply_markup=kb.main_kb)
    await callback.answer("Вы выбрали 7Б")
    await add_user(username=callback.from_user.full_name, tg_id=callback.from_user.id, clas='7Б')


@dp.callback_query(F.data == "picked_start_8A")
async def push_new_user_7A(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(NEW_USER_HELLO, reply_markup=kb.main_kb)
    await callback.answer("Вы выбрали 8А")
    await add_user(username=callback.from_user.full_name, tg_id=callback.from_user.id, clas='8А')


@dp.callback_query(F.data == "picked_start_8B")
async def push_new_user_7A(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(NEW_USER_HELLO, reply_markup=kb.main_kb)
    await callback.answer("Вы выбрали 8Б")
    await add_user(username=callback.from_user.full_name, tg_id=callback.from_user.id, clas='8Б')


@dp.callback_query(F.data == "picked_start_9A")
async def push_new_user_7A(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(NEW_USER_HELLO, reply_markup=kb.main_kb)
    await callback.answer("Вы выбрали 9А")
    await add_user(username=callback.from_user.full_name, tg_id=callback.from_user.id, clas='9А')


@dp.callback_query(F.data == "picked_start_9B")
async def push_new_user_7A(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(NEW_USER_HELLO, reply_markup=kb.main_kb)
    await callback.answer("Вы выбрали 9Б")
    await add_user(username=callback.from_user.full_name, tg_id=callback.from_user.id, clas='9Б')


@dp.callback_query(F.data == "picked_start_10")
async def push_new_user_7A(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(NEW_USER_HELLO, reply_markup=kb.main_kb)
    await callback.answer("Вы выбрали 10 класс")
    await add_user(username=callback.from_user.full_name, tg_id=callback.from_user.id, clas='10')


@dp.callback_query(F.data == "picked_start_11")
async def push_new_user_7A(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(NEW_USER_HELLO, reply_markup=kb.main_kb)
    await callback.answer("Вы выбрали 11")
    await add_user(username=callback.from_user.full_name, tg_id=callback.from_user.id, clas='11')


@dp.message(Command('adm'))
async def cmd_help(message: Message, state: FSMContext):
    await bot.send_message(ADMIN, 'Приступим к работе?', reply_markup=adm_panele())
    code = FSInputFile('school_bot.db')
    await bot.send_document(ADMIN, code)


@dp.message(Command('hadm'))
async def cmd_help(message: Message, state: FSMContext):
    await state.set_state(Reg.complaints_user)
    await message.answer(text='Опишите пожалуйся ваш вопрос и администрация бота в скором времени вам ответит')
 #   cursor.execute('INSERT INTO  (username, tg_id, clas) VALUES (?, ?, ?)', (user_name, user_id, '8Б'))


@dp.message(Reg.complaints_user)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(complaints_user=message.text)
    data = await state.get_data()
#    c message.from_user.id, f'{data["complaints_user"]}'))
    await complaints_user(username=message.from_user.full_name, tg_id=message.from_user.id,
                          complaint=data["complaints_user"])
    await message.answer(f'Ваш вопрос отправлен администратору \n'
                         f'Ваш Вопрос: {data["complaints_user"]}')
    await bot.send_message(ADMIN, f'От пользователя пришел вопрос: \n{data["complaints_user"]}',
                           reply_markup=cmd_help_otvet_kb())
    await state.clear()


@dp.callback_query(F.data == "cmd_help_otvet")
async def cmd_help_otvet(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Приступил к поиску вопросов!')
    await state.set_state(Reg.cmd_help_otvet_state)
    await callback.message.answer(await complaints_user_otvet_2())


@dp.message(Reg.cmd_help_otvet_state)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(cmd_help_otvet_state=message.text)
    data = await state.get_data()
    await bot.send_message(await complaints_user_otvet_3(), f'{data["cmd_help_otvet_state"]}')
    await state.clear()
    await message.answer('Ваш ответ отправлен!')
    await complaints_user_otvet_4()

'''
@dp.message(F.photo)
async def cmd(message: Message):
    photo_id = message.photo[-1].file_id
    await message.reply(f'{photo_id}')
'''


@dp.message(F.text.lower() == 'тех. поддержка 👨‍💻')
async def cmd_help(message: Message, state: FSMContext):
    await state.set_state(Reg.complaints_user)
    await message.answer(text='Опишите пожалуйся ваш вопрос и администрация бота в скором времени вам ответит')
 #   cursor.execute('INSERT INTO  (username, tg_id, clas) VALUES (?, ?, ?)', (user_name, user_id, '8Б'))


@dp.message(Reg.complaints_user)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(complaints_user=message.text)
    data = await state.get_data()
#    c message.from_user.id, f'{data["complaints_user"]}'))
    await complaints_user(username=message.from_user.full_name, tg_id=message.from_user.id,
                          complaint=data["complaints_user"])
    await message.answer(f'Ваш вопрос отправлен администратору \n'
                         f'Ваш Вопрос: {data["complaints_user"]}')
    await bot.send_message(ADMIN, f'От пользователя пришел вопрос: \n{data["complaints_user"]}',
                           reply_markup=cmd_help_otvet_kb())
    await state.clear()


@dp.message(F.text.lower() == 'поддержать бот! 💸')
async def cmd_sta(message: Message):
    await message.answer('Hi! я делаю этого бота в одиночку и мне приходится за свой счет платить за хостинг, буду раз если поддержишь монеткой'
                         '')


@dp.message(F.text.lower() == 'подготовка к экзаменам 📝')
async def cmd_sta(message: Message):
    await message.answer('выбери экзамен который тебе нужен!', reply_markup=exams())


# Полезные ссылочки и информация 📌
@dp.message(F.text.lower() == 'полезные ссылочки и информация 📌')
async def cmd_sta(message: Message):
    await message.answer('Держи интересные ссылочки', reply_markup=links())
    await message.answer('В будущем тут будут материалы по темам из уроков')


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
    await def_com.set_bot_commands(bot)
    await db_start()
    await dp.start_polling(bot)


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")