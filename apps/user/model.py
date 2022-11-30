# -*- coding=utf-8 -*-
# @Time: 2022/11/27 10:29
# @Author: John
# @File: model.py
# @Software: PyCharm
# class User():
#     def __init__(self,username,password,phone=None):
#         self.username=username
#         self.password=password
#         self.phone=phone
#
#     def __str__(self):
#         return self.username
from datetime import datetime
from ext import db
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(15),nullable=False)
    password = db.Column(db.String(12),nullable=False)
    phone = db.Column(db.String(11),unique=True)
    email = db.Column(db.String(20))
    # isDeleted=db.Column(db.String(1))
    rdatetime=db.Column(db.DateTime,default=datetime.now())


    def __str__(self):
        return self.username
