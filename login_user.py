import sqlite3

def loginUserDB(login, password):
    try:
        with sqlite3.connect("DataBase/Base/RegisterUserDataBase.db") as db:
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