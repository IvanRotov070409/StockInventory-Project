import sqlite3
import random

def addUserDB(login, user_name, password):
    try:
        with sqlite3.connect("DataBase/Base/RegisterUserDataBase.db", timeout=30) as db:
            c = db.cursor()
            c.execute("SELECT 1 FROM users WHERE login = ?", (login,))
            if c.fetchone():
                return False
            else:
                user_id = random.randint(100000, 199999)
                c.execute("INSERT INTO users (login, user_name, password, user_id) VALUES (?, ?, ?, ?)",
                          (login, user_name, password, user_id))
                return True
    except sqlite3.Error as error:
        print(f"ERROR SQLITE3: {error}")

def loginUserDB(login, password):
    try:
        with sqlite3.connect("DataBase/Base/RegisterUserDataBase.db", timeout=30) as db:
            c = db.cursor()
            c.execute("SELECT 1 FROM users WHERE login = ? AND password = ?", (login, password))
            print(f"User Login\n"
                  f"Login: {login}\n"
                  f"Password: {len(password) * '*'}\n")
            if c.fetchone():
                return True
            else:
                return False
    except sqlite3.Error as error:
        print(f"ERROR SQLITE3: {error}")

def getUserName(login):
    try:
        with sqlite3.connect("DataBase/Base/RegisterUserDataBase.db", timeout=30) as db:
            c = db.cursor()
            c.execute("SELECT user_name FROM users WHERE login = ?", (login,))
            res = c.fetchone()
            user_name = res[0]
            return user_name
    except sqlite3.Error as error:
        print(f"ERROR SQLITE3: {error}")