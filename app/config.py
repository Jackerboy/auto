import os


class BaseConfig:
    # PER_PAGE = 10
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@192.168.239.132:3306/dev01?charset=utf8mb4'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Jack0327#@106.53.68.245:3306/dev01?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PEROJECT_PER_PAGE = 10
    PER_PAGE = 5
    SECRET_KEY = os.urandom(32)

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProdConfig(BaseConfig):
    pass

class TestConfig(BaseConfig):
    DEBUG = True


# 方法一
config = DevelopmentConfig()