'''
A centralized Configuration file of the app
'''
from datetime import timedelta
import os


class Config():
    TESTING = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI') 
    SECRET_KEY = os.getenv('SECRET_KEY')
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)

#psycopg2 config
class PostgresDatabaseConfig():
    def __init__(self):
        #check .env
        self.HOST = os.getenv('HOST')
        self.USER = os.getenv('DB_USER')
        self.PASSWORD = os.getenv('PASSWORD')
        self.PORT = os.getenv('PORT')
        self.DATABASE_NAME = os.getenv('DATABASE_NAME')

    #since psycopg2.connect accept keyword arguments, then you can use **.
    def return_dict(self) -> dict:
        return {
            'host' : self.HOST,
            'dbname' : self.DATABASE_NAME,
            'user' : self.USER,
            'password' : self.PASSWORD,
            'port' : self.PORT
        }