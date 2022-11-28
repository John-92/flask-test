# -*- coding=utf-8 -*-
# @Time: 2022/11/27 9:54
# @Author: John
# @File: settings.py
# @Software: PyCharm
#将配置信息写进类里
class Config():

    DEBUG = True
    #数据库 驱动pymysql://user:password@ip:3306/database
    SQLALCHEMY_DATABASE_URI= 'mysql+pymysql://root:123456@192.168.52.140:3306/flask'
    SQLACHEMY_ECHO=True


class DevelopmentConfig(Config):
    ENV = 'development'


class ProductionConfig(Config):
    pass

