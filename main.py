import asyncio
import os
import dotenv
import logging
import sys
import sqlite3 as sq
import random

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
    vopros_russ = State()
    answer_to_the_question_1 = State()
    answer_to_the_question_2 = State()
    answer_to_the_question_3 = State()
    teacher_answer_offset_1 = State()
    teacher_answer_offset_2 = State()
    teacher_answer_offset_3 = State()


# здесь происходить ответ на команду /start
@dp.message(CommandStart())
async def reg_one(message: Message, state: FSMContext):
    start_user = message.answer(
        text='Добро пожаловать в чат бот Botintegral, буду рад вам помочь, но для начала должен вас придупредить что используя бота вы даёте согласие на использвание и хранения ваших данных (под данными имеется в виду имя и фамилия которые указаны в боте, а также ваш ID телеграмма',
        reply_markup=kb.main_kb)
    start_new_user = message.answer('Выберете свой класс', reply_markup=choose_class_start())
    admin_new_user = bot.send_message(chat_id=ADMIN,
                                      text=f'В Botintegral зашел новый пользователь \n {message.from_user.full_name}'
                                           f'\nID: {message.from_user.id}')
    hello_user = message.answer('Рад снова увидеть вас!', reply_markup=kb.main_kb)
    await add_user_start(message.from_user.full_name, message.from_user.id, clas=start_new_user, clas_1=start_user,
                         hello_user=hello_user, admin_new_user=admin_new_user)


# Пользователь выбирает в каком он учиться классе
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


# Команда открывает админ панель
@dp.message(Command('adm'))
async def cmd_help(message: Message, state: FSMContext):
    await bot.send_message(ADMIN, 'Приступим к работе?', reply_markup=adm_panele())
    code = FSInputFile('school_bot.db')
    await bot.send_document(ADMIN, code)


@dp.message(Command('code'))
async def cmd_help(message: Message, state: FSMContext):
    db_code = FSInputFile('SQL.py')
    main_code_1 = FSInputFile('main.py')
    default_commands_code = FSInputFile('default_commands.py')
    inline_keyboard_code = FSInputFile('inline_keyboard.py')
    keyboard_code = FSInputFile('keyboard.py')
    requirements_txt = FSInputFile('requirements.txt')
    schedule_code = FSInputFile('schedule.py')
    await message.answer_document(main_code_1)
    await message.answer_document(db_code)
    await message.answer_document(requirements_txt)
    await message.answer_document(inline_keyboard_code)
    await message.answer_document(schedule_code)
    await message.answer_document(keyboard_code)
    await message.answer_document(default_commands_code)


# Команда для того что бы задать интерусующий тебя вопрос администрации
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


# Обработка вопросов от ползователей
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
    await message.answer(
        'Hi! я делаю этого бота в одиночку и мне приходится за свой счет платить за хостинг, буду раз если поддержишь монеткой'
        '')


@dp.message(F.text.lower() == 'подготовка к экзаменам 📝')
async def cmd_sta(message: Message):
    await message.answer('выбери экзамен который тебе нужен!', reply_markup=exams())


@dp.callback_query(F.data == "offset_8")
async def push_schedule_8B(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('Выберите предмет', reply_markup=offset_8_panele())
    await callback.answer("Вы выбрали подготовку к зачётам 8 класса")


@dp.callback_query(F.data == "offset_7")
async def push_schedule_8B(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('Выберите предмет', reply_markup=offset_7_panele())
    await callback.answer("Вы выбрали подготовку к зачётам 7 класса")


@dp.callback_query(F.data == "offset_10")
async def push_schedule_8B(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('Выберите предмет', reply_markup=offset_10_panele())
    await callback.answer("Вы выбрали подготовку к зачётам 10 класса")


@dp.callback_query(F.data == "offset_8_russ")
async def push_schedule_8B(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Выберите интересующий вас пункт", reply_markup=offset_8_panele_russ())


@dp.callback_query(F.data == "offset_8_russ_vopros")
async def push_schedule_8B(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await state.set_state(Reg.vopros_russ)
    await callback.message.answer("Введите номер вопроса \n Например: 13 (всего их 56)\n просьба написать только цифру, в ином случае я сломаюсь :(")


@dp.message(Reg.vopros_russ)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(vopros_russ=message.text)
    data = await state.get_data()
    await message.answer(await offset_russ_8(id=f'{data["vopros_russ"]}'))
    await state.clear()


@dp.callback_query(F.data == "offset_8_russ_vopros_random")
async def push_schedule_8B(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await state.set_state(Reg.answer_to_the_question_1)
    await callback.message.answer("Ухты! Рад что ты решил ответить на 3 случайных вопроса, но учити твои ответы будет видеть и учитель!")
    await callback.message.answer(await offset_russ_random_8_1(tg_id=callback.from_user.id, vopros_1=random.randint(1, 16), username=callback.from_user.full_name))

otvet_offset_list = ["Запомнил твой ответ, теперь следующий вопрос!",
                     "Надеюсь ты ответил(а) верно, но это мы узнаем позже, приступим ко 2-ому вопросу!",
                     "Окей, 1/3 пути пройдена оталось не много",
                     "Как говорится между первым и вторым вопросом перерывчик не большой! )"]


@dp.message(Reg.answer_to_the_question_1)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(answer_to_the_question_1=message.text)
    await state.set_state(Reg.answer_to_the_question_2)
#    data = await state.get_data()
    await message.answer(otvet_offset_list[random.randint(0, 3)])
    await message.answer(await offset_russ_random_8_2(tg_id=message.from_user.id, vopros_2=random.randint(1, 16)))

otvet_offset_list_2 = ["Запомнил твой ответ, теперь следующий вопрос!",
                       "Интересный факт! если честно и хорошо этот пробный зачет, оценка может оказатся и в журнале! (только положительная)",
                       "Ухты, как здорово, 2/3 пути пройдено осталься последний рывок",
                       "Так и хочу тебе подсказать, но я не понимаю правил русского языка (, поехали дальше"]


@dp.message(Reg.answer_to_the_question_2)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(answer_to_the_question_2=message.text)
    await state.set_state(Reg.answer_to_the_question_3)
    await message.answer(otvet_offset_list_2[random.randint(0, 3)])
    await message.answer(await offset_russ_random_8_3(tg_id=message.from_user.id, vopros_3=random.randint(1, 16)))


@dp.message(Reg.answer_to_the_question_3)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(answer_to_the_question_3=message.text)
    data = await state.get_data()
    await message.answer('Супер! Пару мгновений и я отправлю работу учителю, а тебе хорошего настроения!')
    await offset_russ_random_8_4(tg_id=message.from_user.id,
                                 answer_the_vopros_1=f'{data["answer_to_the_question_1"]}',
                                 answer_the_vopros_2=f'{data["answer_to_the_question_2"]}',
                                 answer_the_vopros_3=f'{data["answer_to_the_question_3"]}')
    await bot.send_message(await offset_russ_random_8_15(), """
    Один(-а) учени(к / ца) выполил(-а) пробный зачёт""", reply_markup=offset_random_answer())
    await bot.send_message(await offset_russ_random_8_16(), """
    Один(-а) учени(к / ца) выполил(-а) пробный зачёт""", reply_markup=offset_random_answer())
    await state.clear()


@dp.message(Command('offset_russ'))
async def teacher_answer(message: Message, state: FSMContext):
    answer_not = message.answer('Всю базу данных просмотрел, а ответов от учеников нет 😔')
    not_teacher = message.answer('Хммм мне кажется или вы не учитель? Если я ошибаюсь обратитесь в поддержку.')
    if await offset_russ_random_8_7(tg_id=message.from_user.id, not_teacher=not_teacher) == 1:
        await state.set_state(Reg.teacher_answer_offset_1)
        await message.answer('Вопрос выпавший ученику:\n' + await offset_russ_random_8_5(tg_id=message.from_user.id,
                                                                                         answer_not=answer_not,
                                                                                         not_teacher=not_teacher))
        await message.answer('Ответ ученика на вопрос:\n' + await offset_russ_random_8_6(tg_id=message.from_user.id,
                                                                                         answer_not=answer_not,
                                                                                         not_teacher=not_teacher))


@dp.callback_query(F.data == "offset_random_answer")
async def push_schedule_8B(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    answer_not = callback.message.answer('Всю базу данных просмотрел, а ответов от учеников нет 😔')
    not_teacher = callback.message.answer('Хммм мне кажется или вы не учитель? Если я ошибаюсь обратитесь в поддержку.')
    await state.set_state(Reg.teacher_answer_offset_1)
    await callback.message.answer('Вопрос выпавший ученику:\n' + await offset_russ_random_8_5(
        tg_id=callback.from_user.id,
        answer_not=answer_not,
        not_teacher=not_teacher))
    await callback.message.answer('Ответ ученика на вопрос:\n' + await offset_russ_random_8_6(
        tg_id=callback.from_user.id,
        answer_not=answer_not,
        not_teacher=not_teacher))


@dp.message(Reg.teacher_answer_offset_1)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(teacher_answer_offset_1=message.text)
    answer_not = message.answer('Всю базу данных просмотрел, а ответов от учеников нет 😔')
    await message.answer('Вопрос выпавший ученику:\n' + await offset_russ_random_8_8(answer_not=answer_not))
    await message.answer('Ответ ученика на вопрос:\n' + await offset_russ_random_8_9())
    await state.set_state(Reg.teacher_answer_offset_2)


@dp.message(Reg.teacher_answer_offset_2)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(teacher_answer_offset_2=message.text)
    answer_not = message.answer('Всю базу данных просмотрел, а ответов от учеников нет 😔')
    await message.answer('Вопрос выпавший ученику:\n' + await offset_russ_random_8_10(answer_not=answer_not))
    await message.answer('Ответ ученика на вопрос:\n' + await offset_russ_random_8_11())
    await state.set_state(Reg.teacher_answer_offset_3)


@dp.message(Reg.teacher_answer_offset_3)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(teacher_answer_offset_3=message.text)
    data = await state.get_data()
    answer_not = message.answer('Всю базу данных просмотрел, а ответов от учеников нет 😔')
    await bot.send_message(await offset_russ_random_8_12(), await offset_russ_random_8_13())
    await bot.send_message(await offset_russ_random_8_12(), f"{data['teacher_answer_offset_1']}")
    await bot.send_message(await offset_russ_random_8_12(), await offset_russ_random_8_8(answer_not=answer_not))
    await bot.send_message(await offset_russ_random_8_12(), f"{data['teacher_answer_offset_2']}")
    await bot.send_message(await offset_russ_random_8_12(), await offset_russ_random_8_10(answer_not=answer_not))
    await bot.send_message(await offset_russ_random_8_12(), f"{data['teacher_answer_offset_3']}")
    await message.answer('Все ваши ответы я отправил ученику')
    await offset_russ_random_8_14(answer_the_vopros_1=f'{data["teacher_answer_offset_1"]}',
                                  answer_the_vopros_2=f'{data["teacher_answer_offset_2"]}',
                                  answer_the_vopros_3=f'{data["teacher_answer_offset_3"]}')
    # await offset_russ_random_8_4(tg_id=message.from_user.id,
    #                              answer_the_vopros_1=f'{data["answer_to_the_question_1"]}',
    #                              answer_the_vopros_2=f'{data["answer_to_the_question_2"]}',
    #                              answer_the_vopros_3=f'{data["answer_to_the_question_3"]}')
    await state.clear()


@dp.callback_query(F.data == "offset_7_russ")
async def push_schedule_8B(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await state.set_state(Reg.vopros_russ)
    await callback.message.answer("Введите номер вопроса \n Например: 13 (всего их 20)\n просьба написать только цифру, в ином случае я сломаюсь :(")


@dp.message(Reg.vopros_russ)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(vopros_russ=message.text)
    data = await state.get_data()
    await message.answer(await offset_russ_8(id=f'{data["vopros_russ"]}'))
    await state.clear()


@dp.callback_query(F.data == "offset_10_russ")
async def push_schedule_8B(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await state.set_state(Reg.vopros_russ)
    await callback.message.answer("Введите номер вопроса \n Например: 13 (всего их 21)\n просьба написать только цифру, в ином случае я сломаюсь :(")


@dp.message(Reg.vopros_russ)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(vopros_russ=message.text)
    data = await state.get_data()
    await message.answer(await offset_russ_8(id=f'{data["vopros_russ"]}'))
    await state.clear()


@dp.callback_query(F.data == "vpr_all")
async def push_schedule_8B(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('Выберите класс', reply_markup=preparation_vpr())
    await callback.answer("Вы выбрали подготовку к ВПР")


@dp.callback_query(F.data == "prepaaration_vpr_8")
async def push_schedule_8B(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('Выберите предмет', reply_markup=preparation_vpr_8_clas())
    await callback.answer("Вы выбрали подготовку к ВПР 8 класса")


@dp.callback_query(F.data == "prepaaration_vpr_8_info")
async def push_schedule_8B(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('''
    Первое задание:
    Условия: Переведите десячичное число 78 в восьмеричную систему счисления.
    Решение:
    1. 78 / 8 = 9, остаток 6
    2. 9 / 8 = 1, остаток 1
    3. 1 / 8 = 0, остаток 1
    Теперь мы эти числа ставим в обратном порядке

    Ответ: 116

    Комментарии к решению:
    Для того что бы нам перевести число из одной сстемы счисления в другу, надо делить число а систему счисления, а затем результат до конца \
    после чего подставляем остаток и освет последнего решения в обратном порядке, например 46 переведём в двоичную систему
    1. 46 / 2 = 23, остаток 0
    2. 23 / 2 = 11, остаток 1
    3. 11 / 2 = 5, остаток 1
    4. 5 / 2 = 2, остаток 1
    5. 2 / 2 = 1, остаток 0
    Ответ: 101110
    Да понимаю немного запутанно, поэтому прекомендую прорешать несколько такие задачь
    ''')
    await callback.message.answer('''
    Второе задание:
    Условия:
    Какое из чисел а, записанных в двоичной системе, удовлетворяет условию В2(16) < а < 264(8)?
    1) 10110001
    2) 10110011
    3) 10110101
    4) 10100010
    Решение:
    Переводим все числа в 10 систему счисления и сравниваем
    чтобы перевести в десятичую систему применим следующюю формулу
    74 = (7 * 8 (систему счисления) в степени по расположению в данном случае 1) + (4 * 8 (систему счисления) в степени по расположению в данном случае 0) = 56 + 4 = 60(8)
    B2(16) = (11 × 16 ** 1) + (2 × 16 ** 0) = 176 + 2 = 178(10)
    264(8) = (2 * 8 ** 2) + (6 * 8 ** 1) +  (4 * 8 ** 0) = 180
    10110001(2) = 1 × 2 ** 7) + (0 × 2 ** 6) + (1 × 2 ** 5) + (1 × 2 ** 4) + (0 × 2 ** 3) + (0 × 2 ** 2) + (0 × 2 ** 1) + (1 × 2 ** 0) = 128 + 0 + 32 + 16 + 0 + 0 + 0 + 1 = 177(10)
    10110011(2) = (1 × 2 ** 7) + (0 × 2 ** 6) + (1 × 2 ** 5) + (1 × 2 ** 4) + (0 × 2 ** 3) + (0 × 2 ** 2) + (1 × 2 ** 1) + (1 × 2 ** 0) = 128 + 0 + 32 + 16 + 0 + 0 + 2 + 1 = 179(10)
    10110101(2) = (1 × 2 ** 7) + (0 × 2 ** 6) + (1 × 2 ** 5) + (1 × 2 ** 4) + (0 × 2 ** 3) + (1 × 2 ** 2) + (0 × 2 ** 1) + (1 × 2 ** 0) = 128 + 0 + 32 + 16 + 0 + 4 + 0 + 1 = 181(10)
    10100010(2) = (1 × 2 ** 7) + (0 × 2 ** 6) + (1 × 2 ** 5) + (0 × 2 ** 4) + (0 × 2 ** 3) + (0 × 2 ** 2) + (1 × 2 ** 1) + (0 × 2 ** 0) = 128 + 0 + 32 + 0 + 0 + 0 + 2 + 0 = 162(10)

    Ответ: 2
    ''')
    await callback.message.answer("""
    Третье задание:
    Условия: Выполните сложение: 2С(16) + FB(16).
    Ответ запишите в шестнадцатеричной системе счисления.

    Решение:
    Позаимствуем формулу со второго задания
    2C(16) + FB(16) = 117
    2C(16) = (2 * 16 ** 1) + (12 * 16 ** 0) = 44(10)
    FB(16) = (14 * 16 ** 1) + (11 * 16 ** 0) = 235(10)
    44(10) + 235(10) = 279(10)
    279 / 16 = 17, остаток 7
    17 / 16 = 1, остаток 1
    1 / 16 = 0, остаток 1


    Ответ: 117
    """)
    await callback.message.answer('''
    Четвёртое задание:
    Условия:
    Выполните вычитание: 100110(2) – 1011(2).
    Ответ запишите в двоичной системе счисления

    Решение:
    100110(2) = (1 × 2 ** 5) + (0 × 2 ** 4) + (0 × 2 ** 3) + (1 × 2 ** 2) + (1 × 2 ** 1) + (0 × 2 ** 0) = 32 + 0 + 0 + 4 + 2 + 0 = 38(10)
    1011(2) = (1 × 2 ** 3) + (0 × 2 ** 2) + (1 × 2 ** 1) + (1 × 2 ** 0) = 8 + 0 + 2 + 1 = 11(10)
    38 + 11 = 49(10)
    49 / 2 = 24, остаток 1
    24 / 2 = 12, остаток 0
    12 / 2 = 6, остаток 0
    6 / 2 = 3, остаток 0
    3 / 2 = 1, остаток 1
    1 / 2 = 0, остаток 1

    Ответ: 110001(2)
    ''')
    await callback.message.answer('''
    Пятое задание:
    Условия:
    Укажите имя, для которого ЛОЖНО высказывание.
    НЕ (Первая буква гласная) ИЛИ (Последняя буква гласная)
    1) Анна
    2) Максим
    3) Татьяна
    4) Олег

    Комментарийк задаче:
    Слово не меняет смысл на оборот, тоесть в задаче просят найти ложное высказывание в котором не будет в имени первая буква гласная или последняя.
    слово ИЛИ нам говорит что при соблюдение 1 из условий высказывание будет считатся истинным
    Решение: 
    У имени Анна первая и последняя буква гласная => выражение истинное
    У имени Максим 1 и последняя буква согласная => выражение ложное
    у имени Татьяна первая буква согласная, но последняя гласная => выражение истинное
    У имени Олег первая буква гласная, но последняя согласная => выражение истинное

    Ответ: 2
    ''')
    await callback.message.answer_photo(photo=FSInputFile('image/впр инфа.png'),
                                        caption='''
                                        Шестая задача:
                                        ¬ - этот знак означает отрицание (НЕ)
                                        \/ - этот знак обозначает ИЛИ
                                        Решение:
                                        третий столбик мы подписываем как ¬B далее в полях заполяем если B  равна 1, то пишем 0 tckb 0, то пишем 1
                                        четвертый столбик подписываем ¬B \/ A в этом столбце заполнение предстоит более интересное
                                        если А равна 1 то в столбце пишем 1, если в В стоит 1 и в А 0, то пишем 
                                        ''')
    await callback.message.answer("""
    Восьмое задание:
    Условия:
    У исполнителя Удвоитель две команды, которым присвоены номера:
    1. вычти 1
    2. умножь на 2
    Первая из них уменьшает число на экране на 1, вторая удваивает его.
    Составьте алгоритм получения из числа 5 числа 30, содержащий не более 5 команд.
    В ответе запишите только номера команд в соответствующей алгоритму последовательности. 

    Решение:
    его нет, но это задание легко решить методом тыка

    Ответ:
    12212
    """)
    await callback.message.answer_photo(photo=FSInputFile('image/2024-12-08 00.02.08.jpg'))
    await callback.message.answer("""
    Десятая задача:
    Условия:
    Было проведено 9 запусков программы, при которых в качестве значений переменных s и t
    вводились следующие пары чисел (s, t):
    (15, 9); (5, 11); (3, 11); (18, 15); (0, 9); (15, 6); (17, 10); (–4, 5); (2, 10). Сколько было запусков,
    при которых программа напечатала "NO"? 

    Решение:
    первое число это s, второе числ t
    сейчас я раазбеу именно этот код, а последам подсказки по python
    если число s меньше 10 или число t больше 10, то программа выводит "YES"
    под эти условия подходят только числа:
    5, 11; 3, 11

    Ответ: 5, 11; 3, 11  
    """)
    await callback.message.answer("""
    Теперь немного python:
    разберём 10 задачу 
    1 строка) s = int(input())
    2 строка) t = int(input())
    здесь мы создаем переменые которые запоминают то что мы напишем на клавиатуре
    3 строка) if (s < 10) or (t > 10):
    4 строка)   print("YES")
    здесь мы гворим программе если s меньше 10 или t больше 10 выводится сообщение YES
    5 строка)else:
    6 строка)   print("NO")
    здесь мы говорим что бы если не выполняютсяусловия в if то чтобы программа выводила NO
    """)
    await callback.answer("На этом всё, к сожалению я скорее всего не успею подготовить 7 и 9 задачу. \n УДАЧИ НА АКР")
    await callback.answer("Вы выбрали подготовку к ВПР по информатике")
    await callback.answer("Вы выбрали подготовку к ВПР по информатике")


# Полезные ссылочки и информация 📌
@dp.message(F.text.lower() == 'полезные ссылочки и информация 📌')
async def cmd_sta(message: Message):
    await message.answer('Держи интересные ссылочки', reply_markup=links())
    await message.answer('В будущем тут будут материалы по темам из уроков')


# Обработка запросов после нажатия на кнопку расписание
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


# TODO отве на не известные запросы
@dp.callback_query(F.data == "picked_back")
async def picked_back_8B(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Выберите свой класс ниже: ", reply_markup=choose_class())
    await callback.answer("Возвращаю вас на предыдущее окно")


@dp.callback_query(F.data == "back")
async def picked_back_8B(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('Возвращаю вас в главное меню', reply_markup=kb.main_kb())


@dp.message(F.text.lower() == 'назад')
async def all_text(message: Message):
    await message.delete()
    await message.answer('Возвращаю вас в главное меню', reply_markup=kb.main_kb())


# дальше декраторы обрабатывают сообщение без заготовленых ответов
@dp.callback_query(F.data)
async def all_callback(callback: CallbackQuery):
    await callback.answer('Извините, но эта кнопка на этапе разработки')


@dp.message(F.text)
async def all_text(message: Message):
    await message.delete()
    await message.answer(
        'Я точно знал ответ на ваше сообщение, но забыл, давайте сделаем вид что вы нечего не отпрвляли')


@dp.message(Command)
async def cmd_all(message: Message):
    await message.delete()
    await message.answer(
        text='Интересная команда, но на неё я не знаю ответа, давайте сделаем вид что вы нечего не отпрвляли')


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
