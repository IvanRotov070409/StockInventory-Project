import sqlite3

def addUserDB(login, password):
    try:
        with sqlite3.connect("DataBase/Base/IndustUserDataBase.db") as db:
            c = db.cursor()
            c.execute("SELECT 1 FROM users WHERE login = ?", (login,))
            if c.fetchone():
                return False
            else:
                c.execute("INSERT INTO users (login, password) VALUES (?, ?)", (login, password))
                return True
    except sqlite3.Error as e:
        print(f"ERROR SQLITE3: {e}")