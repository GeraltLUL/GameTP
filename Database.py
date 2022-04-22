import math
import sqlite3
import io
import time

class Database:

    # Инициализация
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    # Создание БД
    def create_db(self, nameDb, scriptDbName):
        try:
            conn = sqlite3.connect(nameDb, check_same_thread=False)
            conn.row_factory = sqlite3.Row

            with io.open(scriptDbName, encoding='utf-8') as file:
                self.__db.cursor().executescript(file.read())
            self.__db.commit()

            #self.__db = Database(self.__db)

        except sqlite3.Error as e:
            print("Ошибка создания БД " + str(e))
            return False

        return True

    # Добавление нового пользователя при его регистрации
    def add_item(self, name, email, psw):
        try:
            #self.__cur.execute(f"SELECT COUNT() as 'count' FROM users WHERE email LIKE '{email}'")
            # res = self.__cur.fetchone()
            #
            # if res['count'] > 0:
            #     print("Пользователь с таким email уже существует")
            #     return False

            #hpsw = generate_password_hash(psw)
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO users VALUES(NULL, ?, ?, ?, ?)", (name, email, psw, tm))
            self.__db.commit()

        except sqlite3.Error as e:
            print("Ошибка регистрации пользователя " + str(e))
            return False

        return True

    def get_item(self, user_id):  # by Id
        try:
            with sqlite3.connect("main.db", check_same_thread=False) as con:
                cur = con.cursor()

                cur.execute(f"SELECT * FROM users WHERE id = {user_id} LIMIT 1")
                con.commit()

                res = cur.fetchone()

                if not res:
                    print("Пользователь не найден")
                    return False

                return res

        except sqlite3.Error as e:
            print("Ошибка получения данных из БД " + str(e))

        return False

    def get_item_by_email(self, email):
        try:
            with sqlite3.connect("main.db", check_same_thread=False) as con:
                cur = con.cursor()


                cur.execute(f"SELECT * FROM users WHERE email = '{email}' LIMIT 1")
                con.commit()

                res = cur.fetchone()

                if not res:
                    print("Пользователь не найден")
                    return False

            return res

        except sqlite3.Error as e:
            print("Ошибка получения данных из БД " + str(e))

        return False