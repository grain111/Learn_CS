from flask import Flask
from flask_session import Session

app = Flask(__name__)

from app import routes

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
