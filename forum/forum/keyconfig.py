import os

class Database:
    ENGINE = os.getenv("DATABASE_ENGINE")
    NAME = os.getenv("DB_SCHEMA")
    USER = os.getenv("DB_USER")
    PASSWORD = os.getenv("DB_PASSWORD")
    HOST = os.getenv("DB_HOST")
    PORT = os.getenv("DB_PORT")
    URL = "mysql://root:Lince123@localhost:3306/forumdb"


class Debug:
    DEBUG = os.getenv("DEBUG")