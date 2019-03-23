from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Reactives(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String, nullable=False) #обязательное поле
        vendor_name = db.Column(db.String, nullable=True)
        reactive_count = db.Column(db.Integer, nullable=False) #обязательное поле
        package = db.Column(db.String, nullable=True)
        reactive_catalog = db.Column(db.String, nullable=True)
        
        



            
        def __repr__(self):
            return '<Reactives {}>'.format(self.title)





# Название реактива *
# Производитель - Vendor
# Количество *
# Фасовка 
# Каталожный номер
# Ссылка на реактив на сайте производителя
# Срочность заказа конкретного реактива - “стратегический” или “срочный”  *
# Вид реактивов (будет список на основе кодов ОКДП2)
# Цель заказа 
# Комментарий
# Поставщик - Seller


# пример - class News(db.Model):
#         id = db.Column(db.Integer, primary_key=True)
#         title = db.Column(db.String, nullable=False)
#         url = db.Column(db.String, unique=True, nullable=False)
#         published = db.Column(db.DateTime, nullable=False)
#         text = db.Column(db.Text, nullable=True)
    
#         def __repr__(self):
#             return '<News {} {}>'.format(self.title, self.url)

#пример - связи между таблицами
# from datetime import datetime
# from app import db

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=True)
#     password_hash = db.Column(db.String(128))
#     posts = db.relationship('Post', backref='author', lazy='dynamic')

#     def __repr__(self):
#         return '<User {}>'.format(self.username)

# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.String(140))
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#     def __repr__(self):
#         return '<Post {}>'.format(self.body)