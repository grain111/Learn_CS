import os

class Config():
    SECRET_KEY = os.getenv("SECRET_KEY") or 'secret'
    # Configure session to use filesystem
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"
