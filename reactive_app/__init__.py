from flask import Flask
# from config import Config
from reactive_app.model import db
from flask import render_template

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    @app.route('/index')
    # def index():
    #     return "Добро пожаловать в мир реактивов"
    def index():
        user = {'user_name': 'Наталья'}
        reactives1 = [
            {'reactive_name': 'Хлорид натрия'},
            {'reactive_name': 'Меркаптанчик'}
        ]
        return render_template('index.html', title='Home', user = user, reactives1=reactives1)
    return app