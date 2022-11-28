# -*- coding=utf-8 -*-
# @Time: 2022/11/27 10:29
# @Author: John
# @File: model.py
# @Software: PyCharm
class User():
    def __init__(self,username,password,phone=None):
        self.username=username
        self.password=password
        self.phone=phone

    def __str__(self):
        return self.username