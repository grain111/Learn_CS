from flask import Flask
from flask_session import Session
from flask_socketio import SocketIO

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
Session(app)
socketio = SocketIO(app, manage_session=False)

from app import routes
