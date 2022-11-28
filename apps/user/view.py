# -*- coding=utf-8 -*-
# @Time: 2022/11/27 10:25
# @Author: John
# @File: view.py
# @Software: PyCharm
from flask import Blueprint, request, redirect, render_template

from apps.user.model import User

user_bp=Blueprint('user',__name__)

#创建user集合，用于去重
users= []

@user_bp.route("/")
def user_center():
    # return "user center"
    return render_template('base.html')

@user_bp.route("/register",methods=['GET','POST'])
def user_register():
    if request.method=="POST":
        #获取form表单里的参数
        username=request.form.get("username")
        password=request.form.get("password")
        repassword=request.form.get("repassword")
        phone=request.form.get("phone")
        if password == repassword:

            for user in users:
                if username == user.username:
                    return render_template("user/register.html",msg="用户已存在")
            user=User(username=username,password=password,phone=phone)
            users.append(user)
            return redirect('/')
    return render_template("user/register.html")

@user_bp.route("/del")
def del_user():
    #1、获取请求信息中的username request.args是获取url的参数，比如？key=jjj
    username=request.args.get("username")
   #2、查找users列表中的这个username的对象
    for user in users:
        if user.username == username:
            users.remove(user)
            # break
            return '删除成功'
    else:
        return '删除失败'



# class UserResouce(Resource):

