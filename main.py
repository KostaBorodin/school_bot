import asyncio
import sqlite3 as sq

from config import TOKEN, ADMIN

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
  email TEXT NOT NULL,
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
    if user[2] == user_id:
        x += 1
    if x >= 1:
        print('новых пользователей нету')
    else:
        cursor.execute('INSERT INTO Users (username, tg_id, clas) VALUES (?, ?, ?)', (user_name, user_id, '8Б'))
        connection.commit()
        print('Новый пользователь добавлен: ', user_id)
      #  print(user[2])


bot = Bot(token=TOKEN)
dp = Dispatcher()
def new_user(user_tg_id, user_name):
  cursor.execute('INSERT INTO Users (username, tg_id, clas) VALUES (?, ?, ?)', (user_name, user_tg_id, '8Б'))

class Reg(StatesGroup):
    clas_user = State()


# здесь происходить ответ на команду /start
@dp.message(CommandStart())
async def reg_one(message: Message):
#   await state.set_state(Reg.clas_user)
    await message.answer(text='Добро пожаловать в чат бот Botintegral, буду рад вам помочь, но для начала должен вас придупредить что используя бота вы даёте согласие на использвание и хранения ваших данных (под данными имеется в виду имя и фамилия которые указаны в боте, а также ваш ID телеграмма')
    await bot.send_message(1410371678, f'В Botintegral зашел пользователь \n{message.from_user.first_name} {message.from_user.last_name}'
                                    f'\nID: {message.from_user.id}')
    await cmd_start_db(user_id=message.from_user.id, user_name=message.from_user.full_name)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())