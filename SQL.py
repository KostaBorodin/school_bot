import sqlite3 as sq
import main as m


async def db_start():
    global connection, cursor

    connection = sq.connect('school_bot.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
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

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Vopros_offset_russ (
    id INTEGER PRIMARY KEY,
    offset_russ_vopros_7 TEXT NOT NULL,
    offset_russ_otvet_7 TEXT NOT NULL,
    offset_russ_vopros_8 TEXT NOT NULL,
    offset_russ_otvet_8 TEXT NOT NULL,
    offset_russ_vopros_10 TEXT NOT NULL,
    offset_russ_otvet_10 TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Otvets_offset_russ (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    tg_id INTEGER NOT NULL,
    vopros_1 INTERGER NOT NULL,
    vopros_2 INTERGER NOT NULL,
    vopros_3 INTERGER NOT NULL,
    answer_the_vopros_1 TEXT NOT NULL,
    answer_the_vopros_2 TEXT NOT NULL,
    answer_the_vopros_3 TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Otvets_offset_teacher (
    id INTEGER PRIMARY KEY,
    tg_id INTEGER NOT NULL,
    answer_the_vopros_1 TEXT NOT NULL,
    answer_the_vopros_2 TEXT NOT NULL,
    answer_the_vopros_3 TEXT NOT NULL
    )
    ''')
    connection.commit()


async def get_all_users():
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    return users


async def add_user(username, tg_id, clas):
    user = cursor.execute(f"SELECT 1 FROM Users WHERE tg_id == {tg_id}").fetchone()
    if not user:
        cursor.execute("INSERT INTO Users (username, tg_id, clas) VALUES(?, ?, ?)", (username, tg_id, clas))
        connection.commit()


async def add_user_start(username, tg_id, clas, clas_1, admin_new_user, hello_user):
    user = cursor.execute(f"SELECT 1 FROM Users WHERE tg_id == {tg_id}").fetchone()
    if not user:
        await clas_1
        await clas
        await admin_new_user
        connection.commit()
    else:
        await hello_user


# TODO Начало обработки вопроса от пользователя
async def complaints_user(username, tg_id, complaint):
    cursor.execute("INSERT INTO Сomplaints (username, tg_id, complaint) VALUES(?, ?, ?)",
                   (username, tg_id, complaint))
    connection.commit()


async def complaints_user_otvet():
    user = cursor.execute(f"SELECT 1 FROM Сomplaints WHERE id == {1}").fetchone()
    if not user:
        print('жалоб нет')
    else:
        cursor.execute(f"SELECT * FROM Сomplaints WHERE id == {1}")
        users = cursor.fetchall()
        for user in users:
            otvet_user = user[3]


async def complaints_user_otvet_2():
    cursor.execute('SELECT * FROM Сomplaints')
    first_user = cursor.fetchone()
    first_user_user = first_user[3]
    return first_user_user


async def complaints_user_otvet_3():
    cursor.execute('SELECT * FROM Сomplaints')
    first_user = cursor.fetchone()
    first_user_id = first_user[2]
    return first_user_id


'''
# Выбираем первого пользователя
cursor.execute('SELECT * FROM Users')
first_user = cursor.fetchone()
print(first_user)
'''


async def complaints_user_otvet_4():
    cursor.execute('SELECT * FROM Сomplaints')
    first_user = cursor.fetchone()
    first_user_id = first_user[0]
    cursor.execute('DELETE FROM Сomplaints WHERE id = ?', (first_user_id,))
    connection.commit()


async def offset_russ_7(id):
    user = cursor.execute(f"SELECT 1 FROM Vopros_offset_russ WHERE id == {int(id)}").fetchone()
    if not user:
        print("Hello world!")
    else:
        cursor.execute(f"SELECT * FROM Vopros_offset_russ WHERE id == {int(id)}")
        users = cursor.fetchall()
        for user in users:
            otvet_user = user[1]
            return otvet_user


async def offset_russ_8(id):
    user = cursor.execute(f"SELECT 1 FROM Vopros_offset_russ WHERE id == {int(id)}").fetchone()
    if not user:
        print("Hello world!")
    else:
        cursor.execute(f"SELECT * FROM Vopros_offset_russ WHERE id == {int(id)}")
        users = cursor.fetchall()
        for user in users:
            otvet_user = user[3]
            return otvet_user


async def offset_russ_random_8_1(tg_id, username, vopros_1):
    user = cursor.execute(f"SELECT 1 FROM Otvets_offset_russ WHERE tg_id == {tg_id}").fetchone()
    if not user:
        cursor.execute("INSERT INTO Otvets_offset_russ (username, tg_id, vopros_1, vopros_2, vopros_3, answer_the_vopros_1, answer_the_vopros_2, answer_the_vopros_3) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (username, tg_id, vopros_1, 0, 0, '-', '-', '-'))
        connection.commit()
    else:
        cursor.execute("UPDATE Otvets_offset_russ SET vopros_1 = ? WHERE tg_id = ?", (vopros_1, tg_id))
        connection.commit()
    cursor.execute(f"SELECT * FROM Vopros_offset_russ WHERE id == {vopros_1}")
    users = cursor.fetchall()
    for user in users:
        otvet_user = user[3]
        return otvet_user


async def offset_russ_random_8_2(tg_id, vopros_2):
    cursor.execute("UPDATE Otvets_offset_russ SET vopros_2 = ? WHERE tg_id = ?", (vopros_2, tg_id))
    connection.commit()
    cursor.execute(f"SELECT * FROM Vopros_offset_russ WHERE id == {vopros_2}")
    users = cursor.fetchall()
    for user in users:
        otvet_user = user[3]
        return otvet_user


async def offset_russ_random_8_3(tg_id, vopros_3):
    cursor.execute("UPDATE Otvets_offset_russ SET vopros_3 = ? WHERE tg_id = ?", (vopros_3, tg_id))
    connection.commit()
    cursor.execute(f"SELECT * FROM Vopros_offset_russ WHERE id == {vopros_3}")
    users = cursor.fetchall()
    for user in users:
        otvet_user = user[3]
        return otvet_user


async def offset_russ_random_8_4(tg_id, answer_the_vopros_1, answer_the_vopros_2, answer_the_vopros_3):
    cursor.execute("UPDATE Otvets_offset_russ SET answer_the_vopros_1 = ? WHERE tg_id = ?", (answer_the_vopros_1, tg_id))
    cursor.execute("UPDATE Otvets_offset_russ SET answer_the_vopros_2 = ? WHERE tg_id = ?", (answer_the_vopros_2, tg_id))
    cursor.execute("UPDATE Otvets_offset_russ SET answer_the_vopros_3 = ? WHERE tg_id = ?", (answer_the_vopros_3, tg_id))
    connection.commit()


async def offset_russ_random_8_5(tg_id, answer_not, not_teacher):
    user = cursor.execute(f"SELECT * FROM Users WHERE tg_id == {int(tg_id)}").fetchone()
    if user[3] == 'creator' or user[3] == 'teacher':
        answer = cursor.execute(f"SELECT 1 FROM Otvets_offset_russ WHERE id == {1}").fetchone()
        if not answer:
            await answer_not
        else:
            answer_1 = cursor.execute(f"SELECT * FROM Otvets_offset_russ WHERE id == {1}").fetchone()
            answer_2 = cursor.execute(f"SELECT * FROM Vopros_offset_russ WHERE id == {answer_1[3]}").fetchone()
            return answer_2[3]
    else:
        await not_teacher


async def offset_russ_random_8_6(tg_id, answer_not, not_teacher):
    user = cursor.execute(f"SELECT * FROM Users WHERE tg_id == {int(tg_id)}").fetchone()
    if user[3] == 'creator' or user[3] == 'teacher':
        answer = cursor.execute(f"SELECT 1 FROM Otvets_offset_russ WHERE id == {1}").fetchone()
        if not answer:
            await answer_not
        else:
            answer_1 = cursor.execute(f"SELECT * FROM Otvets_offset_russ WHERE id == {1}").fetchone()
            return answer_1[6]
    else:
        await not_teacher


async def offset_russ_random_8_7(tg_id, not_teacher):
    user = cursor.execute(f"SELECT * FROM Users WHERE tg_id == {int(tg_id)}").fetchone()
    if user[3] == 'creator' or user[3] == 'teacher':
        return 1
    else:
        await not_teacher


async def offset_russ_random_8_8(answer_not):
    answer = cursor.execute(f"SELECT 1 FROM Otvets_offset_russ WHERE id == {1}").fetchone()
    if not answer:
        await answer_not
    else:
        answer_1 = cursor.execute(f"SELECT * FROM Otvets_offset_russ WHERE id == {1}").fetchone()
        answer_2 = cursor.execute(f"SELECT * FROM Vopros_offset_russ WHERE id == {answer_1[4]}").fetchone()
        return answer_2[3]


async def offset_russ_random_8_9():
    answer_1 = cursor.execute(f"SELECT * FROM Otvets_offset_russ WHERE id == {1}").fetchone()
    return answer_1[7]


async def offset_russ_random_8_10(answer_not):
    answer = cursor.execute(f"SELECT 1 FROM Otvets_offset_russ WHERE id == {1}").fetchone()
    if not answer:
        await answer_not
    else:
        answer_1 = cursor.execute(f"SELECT * FROM Otvets_offset_russ WHERE id == {1}").fetchone()
        answer_2 = cursor.execute(f"SELECT * FROM Vopros_offset_russ WHERE id == {answer_1[5]}").fetchone()
        return answer_2[3]


async def offset_russ_random_8_11():
    answer_1 = cursor.execute(f"SELECT * FROM Otvets_offset_russ WHERE id == {1}").fetchone()
    return answer_1[8]


async def offset_russ_random_8_12():
    answer_1 = cursor.execute(f"SELECT * FROM Otvets_offset_russ WHERE id == {1}").fetchone()
    return answer_1[2]


async def offset_russ_random_8_13():
        answer_1 = cursor.execute(f"SELECT * FROM Otvets_offset_russ WHERE id == {1}").fetchone()
        answer_2 = cursor.execute(f"SELECT * FROM Vopros_offset_russ WHERE id == {answer_1[3]}").fetchone()
        return answer_2[3]


async def offset_russ_random_8_14(answer_the_vopros_1, answer_the_vopros_2, answer_the_vopros_3):
    answer_1 = cursor.execute(f"SELECT * FROM Otvets_offset_russ WHERE id == {1}").fetchone()
    cursor.execute(
        "INSERT INTO Otvets_offset_teacher (tg_id, answer_the_vopros_1, answer_the_vopros_2, answer_the_vopros_3) VALUES(?, ?, ?, ?)",
        (answer_1[2], answer_the_vopros_1, answer_the_vopros_2, answer_the_vopros_3))
    cursor.execute('DELETE FROM Otvets_offset_russ WHERE id = ?', (1,))
    connection.commit()


async def offset_russ_random_8_15():
    user = cursor.execute(f"SELECT * FROM Users WHERE id == {4}").fetchone()
    return user[2]


async def offset_russ_random_8_16():
    user = cursor.execute(f"SELECT * FROM Users WHERE id == {1}").fetchone()
    return user[2]


async def offset_russ_10(id):
    user = cursor.execute(f"SELECT 1 FROM Vopros_offset_russ WHERE id == {int(id)}").fetchone()
    if not user:
        print("Hello world!")
    else:
        cursor.execute(f"SELECT * FROM Vopros_offset_russ WHERE id == {int(id)}")
        users = cursor.fetchall()
        for user in users:
            otvet_user = user[5]
            return otvet_user


# TODO Завершение обработки ответа  на вопрос пользователя

'''
async def complaints_user_otvet(not_complaint, otvet_complaint):
    user = cursor.execute(f"SELECT 1 FROM Сomplaints WHERE id == {1}").fetchone()
    if not user:

    else:
        await 
'''