import asyncio
import sqlite3 as sq

from config import TOKEN
import keabort as kb

from aiogram import Dispatcher, Bot, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

connection = sq.connect('school_bot.db')
cursor = connection.cursor()

cursor.execute('''
  CREATE TABLE IF NOT EXISTS Users (
  id INTEGER PRIMARY KEY,
  username TEXT NOT NULL,
  tg_id INTEGER,
  clas TEXT NOT NULL
  )
  ''')

cursor.execute('''
  CREATE TABLE IF NOT EXISTS Сomplaints (
  id INTEGER PRIMARY KEY,
  username TEXT NOT NULL,
  tg_id INTEGER,
  complaint TEXT NOT NULL
  )
  ''')

cursor.execute("""
  CREATE TABLE IF NOT EXISTS admins(
  id INTEGER PRIMARY KEY,
  tg_id_admin INTEGER NOT NULL,
  username TEXT NOT NULL,
  name TEXT NOT NULL,
  password TEXT NOT NULL
  )
  """)
connection.commit()
# Выбираем всех пользователей
cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()

# Выводим результаты
async def cmd_start_db(user_id, user_name):
    cursor.execute('SELECT COUNT(*) FROM Users')
#  total_users = cursor.fetchone()[0]
    x = 0
    for user in users:
        print(user[2])
        if user[2] == user_id:
            x += 1
    if x >= 1:
        print('Новых пользователей нет')
    else:
        cursor.execute('INSERT INTO Users (username, tg_id, clas) VALUES (?, ?, ?)', (user_name, user_id, '8Б'))
        connection.commit()
        connection.close()
    # print(user[2])


bot = Bot(token=TOKEN)
dp = Dispatcher()


class Reg(StatesGroup):
    clas_user = State()
    complaints_user = State()

# здесь происходить ответ на команду /start
@dp.message(CommandStart())
async def reg_one(message: Message):
    await message.answer(text='Добро пожаловать в чат бот Botintegral, буду рад вам помочь, но для начала должен вас придупредить что используя бота вы даёте согласие на использвание и хранения ваших данных (под данными имеется в виду имя и фамилия которые указаны в боте, а также ваш ID телеграмма', reply_markup=kb.main_kb)
    await bot.send_message(1410371678, f'В Botintegral зашел новый пользователь \n {message.from_user.full_name}'
                            f'\nID: {message.from_user.id}')
#   await state.set_state(Reg.clas_user)
    await cmd_start_db(user_id=message.from_user.id, user_name=message.from_user.full_name)


@dp.message(Command('hadm'))
async def cmd_help(message: Message, state: FSMContext):
    await state.set_state(Reg.complaints_user)
    await message.answer(text='Опишите пожалуйся ваш вопрос и администрация бота в скором времени вам ответит')
 #   cursor.execute('INSERT INTO  (username, tg_id, clas) VALUES (?, ?, ?)', (user_name, user_id, '8Б'))


@dp.message(Reg.complaints_user)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(complaints_user=message.text)
    data = await state.get_data()
    cursor.execute('INSERT INTO Сomplaints (username, tg_id, complaint) VALUES (?, ?, ?)', (message.from_user.full_name, message.from_user.id, f'{data["complaints_user"]}'))
    await message.answer(f'Ваш вопрос отправлен администратору {data["complaints_user"]}')
    connection.commit()
    await state.clear()

'''
@dp.message(F.photo)
async def cmd(message: Message):
    photo_id = message.photo[-1].file_id
    await message.reply(f'{photo_id}')
'''

@dp.message()
async def cmd_sta(message: Message):
    if message.text.lower() == 'расписание 🗓':
        await message.answer_photo('AgACAgIAAxkBAAJ06WcyMDMWFoiCv4Lg7yV-Cf9pN34AA_3hMRvQ45hJHUhvO3SJTcsBAAMCAAN5AAM2BA')
        await message.answer('''
Расписание уроков 8Б

ПОНЕДЕЛЬНИК:
[ 8:30 - 9:10   ] Разговоры о не важном
[ 9:20 - 10:00  ] Информатика
[ 10:10 - 10:50 ] ОПД
[ 11:15 - 11:55 ] Литература
[ 12:20 - 13:00 ] Русский язык
[ 13:15 = 13:55 ] Иностранный язык
[ 14:05 - 14:45 ] Физкультура

ВТОРНИК:
[ 8:30 - 9:10   ] Французкий язык
[ 9:20 - 10:00  ] География
[ 10:10 - 10:50 ] Вероятность и статистика
[ 11:15 - 11:55 ] Химия
[ 12:20 - 13:00 ] Русский язык

СРЕДА:
[ 8:30 - 9:10   ] История 
[ 9:20 - 10:00  ] Русский язык
[ 10:10 - 10:50 ] Физкультура
[ 11:15 - 11:55 ] Химия
[ 12:20 - 13:00 ] Алгебра
[ 13:15 = 13:55 ] Обществознание
    
ЧЕТВЕРГ:
[ 8:30 - 9:10   ] Биология
[ 9:20 - 10:00  ] Литература
[ 10:10 - 10:50 ] Музыка
[ 11:15 - 11:55 ] Алгебра
[ 12:20 - 13:00 ] Алгебра

ПЯТНИЦА:
[ 9:20 - 10:00  ] Физика
[ 10:10 - 10:50 ] Геометрия
[ 11:15 - 11:55 ] Биология
[ 12:20 - 13:00 ] История
[ 13:15 = 13:55 ] История

СУББОТА:
[ 8:30 - 9:10   ] География
[ 9:20 - 10:00  ] ОБЗР
[ 10:10 - 10:50 ] Физика
[ 11:05 - 11:45 ] Физкультура
[ 12:00 - 12:40 ] Геометия
[ 12:50 = 13:30 ] Труд''')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())