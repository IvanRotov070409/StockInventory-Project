import sqlite3
import random
import json
import re
import uuid

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

def get_shops_by_user():
    with open('assets/user.json', 'r', encoding='windows-1251') as f:
        user_data = json.load(f)
        email = user_data['email']
    try:
        with sqlite3.connect("DataBase/Base/RegisterUserDataBase.db", timeout=30) as db:
            c = db.cursor()
            c.execute("SELECT user_id FROM users WHERE login = ?", (email,))
            user_id_result = c.fetchone()

            if not user_id_result:
                print(f"Не найден user_id для email: {email}")
                return None

            user_id = user_id_result[0]
            c.execute("SELECT name, shop_id FROM shop WHERE user_id = ?", (user_id,))
            shops = c.fetchall()
            total_shops = len(shops)
            for name, shop_id in shops:
                pass

            return {
                "total_shops": total_shops,
                "shops": [{"name": name, "shop_id": shop_id} for name, shop_id in shops]
            }

    except sqlite3.Error as error:
        print(f"ERROR SQLITE3: {error}")
        return None


def create_shop_product_table(shop_id):
    db_path = "DataBase/Base/ProductShopDataBase.db"
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        table_name = f'"{shop_id}"'
        create_table_sql = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id_product      TEXT PRIMARY KEY,
            name_product   TEXT NOT NULL,
            about_product  TEXT,
            url_image_product TEXT,
            price_product  TEXT,
            remains_product TEXT,
            weight_product TEXT,
            barcode_product TEXT
        );
        """

        cursor.execute(create_table_sql)
        conn.commit()
        return True


def generate_id():
    return str(uuid.uuid4())[:8]

def add_product_to_shop(name, weight, remains, image, shop_id, about, barcode, price):
    clean_shop_id = re.sub(r'[^a-zA-Z0-9_]', '', shop_id)
    conn = sqlite3.connect('DataBase/Base/ProductShopDataBase.db')
    cursor = conn.cursor()
    try:
        create_table_query = f'''
        CREATE TABLE IF NOT EXISTS "{clean_shop_id}" (
            id_product TEXT,
            name_product TEXT,
            about_product TEXT,
            url_image_product TEXT,
            price_product TEXT,
            remains_product TEXT,
            weight_product TEXT,
            barcode_product TEXT
        )
        '''
        cursor.execute(create_table_query)
        id_product = generate_id()
        data = (
            str(id_product),
            str(name),
            str(about),
            str(image),
            str(price),
            str(remains),
            str(weight),
            str(barcode)
        )
        insert_query = f'''
        INSERT INTO "{clean_shop_id}" (
            id_product,
            name_product,
            about_product,
            url_image_product,
            price_product,
            remains_product,
            weight_product,
            barcode_product
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        '''
        cursor.execute(insert_query, data)
        conn.commit()
        print(f"Продукт с ID {id_product} успешно добавлен в таблицу {clean_shop_id}!")
        return id_product
    except:
        conn.rollback()
    finally:
        conn.close()


def get_products_by_shop(shop_id):
    conn = None
    clean_shop_id = re.sub(r'[^a-zA-Z0-9_]', '', shop_id)

    try:
        conn = sqlite3.connect('DataBase/Base/ProductShopDataBase.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (clean_shop_id,))
        if cursor.fetchone() is None:
            return None
        query = f"""
            SELECT
                id_product,
                name_product,
                about_product,
                url_image_product,
                price_product,
                remains_product,
                weight_product,
                barcode_product
            FROM "{clean_shop_id}"
            ORDER BY name_product;
        """

        cursor.execute(query)
        rows = cursor.fetchall()

        products = []
        for row in rows:
            product = {
                "product_id": row["id_product"],
                "name": row["name_product"],
                "about": row["about_product"],
                "image": row["url_image_product"],
                "price": row["price_product"],
                "remains": row["remains_product"],
                "weight": row["weight_product"],
                "barcode": row["barcode_product"]
            }
            products.append(product)

        return {"products": products}

    except:
        return None
    finally:
        if conn:
            conn.close()

