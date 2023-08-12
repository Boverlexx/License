from flask import Flask
from flask_ngrok import run_with_ngrok
from flask import Flask, render_template
from PySide6 import QtSql
from flask import Flask, request
import datetime
import sqlite3
import pickle
import json
import rsa
import random

client_private_key = pickle.load(open('client_private.key', 'rb'))
server_public_key = pickle.load(open('server_public.key', 'rb'))

class Database:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.initialize()

    def initialize(self):
        self.con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.con.setDatabaseName(self.db_name)
        self.con.open()
        self.con.transaction()
        query = QtSql.QSqlQuery()
        query.exec("""CREATE TABLE IF NOT EXISTS users(
                       id INTEGER PRIMARY KEY NOT NULL,
                       name TEXT,surname TEXT,email TEXT,
                       hwid VARCHAR(64) UNIQUE,lic_key TEXT UNIQUE,
                       date_reg TEXT)""")
        self.con.commit()
        self.con.close()

    # def get_connection(self):
    #     return sqlite3.connect(self.db_name)

    def get_license(self,name: str, surname: str, email: str, hwid: str, lic_key: str, dt_now) -> None:
        self.con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.con.setDatabaseName(self.db_name)
        self.con.open()
        self.con.transaction()
        print(hwid)
        print(lic_key)
        query = QtSql.QSqlQuery()
        if query.exec(f"SELECT hwid FROM users WHERE hwid = '{hwid}'") and query.first():
            result =  'Этот компьютер уже активирован.'
            print('1')
        else:
            if query.exec(f"SELECT lic_key FROM users WHERE lic_key = '{lic_key}'") and query.first():
                print(query.value('lic_key'))
                query.exec(f"SELECT hwid FROM users WHERE hwid NOT IS NULL") and query.first()
                print('Лицензия добавлена.')
                query.exec(f"UPDATE users SET name ='{name}' , surname = '{surname}', email ='{email}', hwid = '{hwid}', date_reg = '{dt_now}' WHERE lic_key = '{lic_key}'")
                # result = (f"{dt_now}" + '\n'+'Добавлена новая лицензия: ' + hwid)
                result = (f"{hwid}")
                print('2')
            else:
                result = 'Оплатите лицензию для этого ПК.'
                print('3')
        self.con.commit()
        return result


db = Database('licens_Menu_V1.db')
app = Flask(__name__)
app.config['DEBUG'] = True
dt_now = datetime.datetime.now()

@app.route('/get_license', methods=['POST'])
def get_license():
    if request.method == 'POST':
        data = request.form['data']
        data = json.loads(rsa.decrypt(bytes.fromhex(data), client_private_key))
        name = data['name']
        surname = data['surname']
        email = data['email']
        hwid = data['hwid']
        lic_key = data['lic_key']
        lic = db.get_license(name, surname, email, hwid,lic_key, dt_now)
        response = rsa.encrypt(json.dumps({'license': lic}).encode('utf-8'), server_public_key).hex()
        return {'data': response}
    return 'Hello World!'

app.run(host='0.0.0.0', port=4567)