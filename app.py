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



#��Ȼ���ã�������Ҫ���룬��Ҫ��ִ��������ʱ��Ҫ�õ����model,���򣬻��Ҳ���ģ�ͺ���
from apps.user.model import User
from apps import create_app
from ext import db

#���һ��Ҫ����main�����⣿��
app = create_app()

migrate = Migrate(app=app, db=db)


if __name__ == '__main__':

    app.run()
