'''
A centralized Configuration file of the app
'''
from datetime import timedelta
import os


class Config():
    TESTING = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI') #postgres/psycopg::/sample
    SECRET_KEY = os.getenv('SECRET_KEY')                #asdjnwe13emskd
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
    #---Session based---
    SESSION_TYPE = 'sqlalchemy'
    SESSION_SQLALCHEMY = create_engine(SQLALCHEMY_DATABASE_URI)
    

#psycopg config
class PostgresDatabaseConfig():
    def __init__(self):
        #check .env
        self.HOST = os.getenv('HOST')
        self.USER = os.getenv('DB_USER')
        self.PASSWORD = os.getenv('PASSWORD')
        self.PORT = os.getenv('PORT')
        self.DATABASE_NAME = os.getenv('DATABASE_NAME')

    #since psycopg.connect accept keyword arguments, then you can use **.
    def return_dict(self) -> dict:
        return {
            'host' : self.HOST,
            'dbname' : self.DATABASE_NAME,
            'user' : self.USER,
            'password' : self.PASSWORD,
            'port' : self.PORT
        }