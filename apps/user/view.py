# -*- coding=utf-8 -*-
# @Time: 2022/11/27 10:25
# @Author: John
# @File: view.py
# @Software: PyCharm
# from operator import or_

from flask import Blueprint, request, redirect, render_template, url_for
from ext import db
from apps.user.model import User

user_bp=Blueprint('user',__name__)

#创建user集合，用于去重
users= []

# @user_bp.route("/")
# def center():
#     user=User.query.filter().all()
#     return render_template('user/center.html',user=user)

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
            #1、找到模型并创建对象，对其进行附值
            user=User(username=username,password=password,phone=phone)
            # users.append(user)
            #2、将user对象添加到session中
            db.session.add(user)
            #3、提交数据
            db.session.commit()
            return redirect('/')
        else:
            msg="用户或密码用问题"
            print("hello")
            return render_template("user/register.html",msg=msg)

    return render_template("user/register.html")

#endpoint给视图函数取别名
# @user_bp.route("/del",endpoint='del')
# def del_user():
#     #1、获取请求信息中的username request.args是获取url的参数，比如？key=jjj
#     username=request.args.get("username")
#    #2、查找users列表中的这个username的对象
#     for user in users:
#         if user.username == username:
#             users.remove(user)
#             # break
#             return '删除成功'
#     else:
#         return '删除失败'

#endpoint给视图函数取别名
@user_bp.route("/del",endpoint='del')
def del_user():
    #1、获取请求信息中的username request.args是获取url的参数，比如？key=jjj
    id=request.args.get('id')
    print(id)
   #2、查找users列表中的这个username的对象

    #删除方式一、逻辑删除
    # user=User.query.get(id)
    # user.isDeleted=True
    # #操作完一定要提交
    # db.session.commit()

    #删除方式二、物理删除
    user=User.query.get(id)
    print(user)
    #将删除的命令添加到缓存中
    db.session.delete(user)
    #操作完一定要提交
    db.session.commit()

    return redirect(url_for('user.user_center'))
    # pass


@user_bp.route("/")
def user_center():
    #继承db.Model的方法
    users=User.query.all()
    print(users)
    return render_template('user/center.html',users=users)
# class UserResouce(Resource):

# 搜索只要get方法就行了
@user_bp.route("/saerch")
def user_search():
    # 获取url中key是search的value
    print("jj")
    search=request.args.get("search")
    # print(search)
    users=User.query.filter(User.username.contains(search))
    return render_template('user/center.html',users=users)


@user_bp.route("/update",endpoint='update',methods=['GET','POST'])
def user_update():
    print("hhh")
    if request.method=='POST':
        id=request.form.get('id')
        print(id)
        username=request.form.get('username')
        phone=request.form.get('phone')
        user=User.query.get(id)
        #对用户信息进行更改
        user.username=username
        user.phone=phone
        db.session.commit()
        return redirect(url_for('user.user_center'))
    else:
        id=request.args.get('id')
        user=User.query.get(id)
        return render_template('user/update.html',user=user)

    # return
    # pass