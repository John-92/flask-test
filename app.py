from flask import Flask,render_template

# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!hh '
#
# @app.route('/test')
# def hello():  # put application's code here
#     return render_template('t1.html')
from flask_migrate import Migrate



#虽然不用，但必须要导入，主要是执行命令行时需要用到这个model,否则，会找不到模型函数
from apps.user.model import User
from apps import create_app
from ext import db

#这个一定要放在main函数外？？
app = create_app()

migrate = Migrate(app=app, db=db)


if __name__ == '__main__':

    app.run()
