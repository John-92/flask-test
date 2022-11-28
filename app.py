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
from apps import create_app

if __name__ == '__main__':
    app=create_app
    app.run(debug=True)
