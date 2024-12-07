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

'''
async def complaints_user_otvet(not_complaint, otvet_complaint):
    user = cursor.execute(f"SELECT 1 FROM Сomplaints WHERE id == {1}").fetchone()
    if not user:
        
    else:
        await 
'''
