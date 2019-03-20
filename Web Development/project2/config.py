import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY") or "secret"
    # Configure session to use filesystem
    SESSION_PERMANENT = True
    SESSION_TYPE = "filesystem"
    PERMANENT_SESSION_LIFETIME = 5 * 60
