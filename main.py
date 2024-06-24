import os
import threading
import webbrowser

from flask import Flask, request
from flask_cors import CORS, cross_origin
from application.application_start import parts, factory
from flask_socketio import SocketIO, emit
import base64
import json
import os
import ssl
import _thread as thread
import websocket
from time import sleep
import sqlite3

app = Flask(__name__)
socketio = SocketIO(app)
app.register_blueprint(parts)
app.register_blueprint(factory)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'application/json'
webbrowser.get('chrome')


conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# cursor.execute('DROP TABLE parts;')
# cursor.execute('DROP TABLE factory;')
# cursor.execute('DROP TABLE factory_parts_mapping;')
#
# cursor.execute('CREATE TABLE IF NOT EXISTS parts ( partId INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, delete_flag INTEGER DEFAULT 0 );')
# cursor.execute('CREATE TABLE IF NOT EXISTS factory ( factoryId INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, longitude REAL NOT NULL, latitude REAL NOT NULL );')
# cursor.execute('CREATE TABLE IF NOT EXISTS factory_parts_mapping ( factoryId INTEGER , partId INTEGER , quantity INTEGER );')


# 提交事务:
conn.commit()
conn.close()

@socketio.on("test_conn")
def message(msg):
    print("message", msg)

def startApplication():
    socketio.run(app, port=2020, host="127.0.0.1", debug=False)
    # startapp.startApp(personInfo)


if __name__ == '__main__':
    t1 = threading.Thread(target=startApplication)
    t1.start()

    current_path = os.path.dirname(__file__)
