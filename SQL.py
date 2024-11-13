import sqlite3 as sq

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
        cursor.execute("INSERT INTO Users (username, tg_id, clas) VALUES(?, ?, ?)",
                    (username, tg_id, clas))
        connection.commit()


async def complaints_user(username, tg_id, complaint):
    cursor.execute("INSERT INTO Complaints (username, tg_id, complaint) VALUES(?, ?, ?)",
                   (username, tg_id, complaint))
    connection.commit()