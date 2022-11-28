# -*- coding=utf-8 -*-
# @Time: 2022/11/27 9:56
# @Author: John
# @File: __init__.py.py
# @Software: PyCharm
from flask import Flask

import settings
from apps.user.view import user_bp
from ext import db




def create_app():
    #指定模板和静态文件的目录,因为Flask默认的template和static路径都在同级目录，如果要定制需要指定
    app=Flask(__name__,template_folder="../templates",static_folder="../static")

    #直接导入flask的settings配置文件
    app.config.from_object(settings.DevelopmentConfig)

    db.init_app(app)
    #注册到蓝图中
    app.register_blueprint(user_bp)
    print(app.url_map)
    return app


