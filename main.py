import sqlite3
from flask import Flask, jsonify, request, send_from_directory, render_template, abort, json, make_response, flash, \
    session, redirect, url_for, g
from Database import Database

# Flask Cofnig
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config.from_object(__name__)

#DataBase Config
DB_MAIN = 'main.db'
dbaseUsers = Database(sqlite3.connect(DB_MAIN))

@app.route('/status')
def status():
    return "True"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        args = request.args

        email = args.get('email')
        psw = args.get('psw')

        res = dbaseUsers.get_item_by_email(email)

        if res == False:
            return "Пользователь не найден"
        else:
            if res[3] == psw:
                return "Пользователь найден, пароль верный"
            else:
                return "Пользователь найден, пароль НЕ верный"

    if request.method == 'POST':
        data = request.form
        email = data['email']
        psw = data['psw']

        res = dbaseUsers.get_item_by_email(email)
        print("1121")
        if res == False:
            return "Пользователь не найден"
        else:
            if res[3] == psw:
                return "Пользователь найден, пароль верный"
            else:
                return "Пользователь найден, пароль НЕ верный"



if __name__ == '__main__':
    #dbaseUsers.create_db(DB_MAIN, "sq_db.sql")
    #dbaseUsers.add_item('John', 'john@mail.ru', '123456')
    #dbaseUsers.add_item('Ben', 'ben@mail.ru', 'qwerty')
    #dbaseUsers.add_item('Tom', 'tom@mail.ru', '1q2w3e')

    app.run(debug=True, port=5000, host='0.0.0.0')