from flask import Flask
# from config import Config
from reactive_app.model import db

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    @app.route('/index')
    def index():
        return "Добро пожаловать в мир реактивов"

    return app