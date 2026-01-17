import sqlite3
import random
import json

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


def addMag(name, shop_id):
    try:
        with open('assets/user.json', 'r', encoding='windows-1251') as json_file:
            user_data = json.load(json_file)
            email = user_data.get('email')

            if not email:
                return False
        with sqlite3.connect("DataBase/Base/RegisterUserDataBase.db", timeout=30) as db:
            c = db.cursor()
            c.execute("SELECT user_id FROM users WHERE login = ?", (email,))
            user_id_result = c.fetchone()

            if not user_id_result:
                print(f"ERROR: User with email '{email}' not found in database")
                return False

            user_id = user_id_result[0]
            c.execute("SELECT 1 FROM shop WHERE name = ? AND shop_id = ?", (name, shop_id))
            if c.fetchone():
                return False
            else:
                c.execute("INSERT INTO shop (name, user_id, shop_id) VALUES (?, ?, ?)",
                          (name, user_id, shop_id))
                return True

    except sqlite3.Error as error:
        print(f"ERROR SQLITE3: {error}")
        return False

