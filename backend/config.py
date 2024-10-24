from decouple import config
import os


class Config:
    SECRET_KEY=config('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS=config('SQLALCHEMY_TRACK_MODIFICATIONS', cast=bool)


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI="mssql+pymssql://sa:w1n0n4#69@10.10.10.201:1433/Solares"
    DEBUG=True
    SQLALCHEMY_ECHO=True
    

class ProdConfig(Config):
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI="sqlite:///dev.db"
    SQLALCHEMY_ECHO=False
    TESTING=True
    