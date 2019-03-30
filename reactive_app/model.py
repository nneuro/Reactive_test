from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Reactives(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String, nullable=False) #обязательное поле
        vendor_name = db.Column(db.String, nullable=True)
        reactive_count = db.Column(db.Integer, nullable=False) #обязательное поле
        package = db.Column(db.String, nullable=True)
        reactive_catalog = db.Column(db.String, nullable=True)
        url_reactive = db.Column(db.String, nullable=True)
        urgency = db.Column(db.String, nullable=True)
        reactive_sort = db.Column(db.String, nullable=True)
        reactive_aim = db.Column(db.String, nullable=True)
        reactive_comment = db.Column(db.String, nullable=True)
        seller = db.Column(db.String, nullable=True)
        order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))

        def __repr__(self):
            return '<Reactives {}>'.format(self.title)

class Orders(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        order_date_published = db.Column(db.DateTime, default=datetime.utcnow)
        reactive_in_order_id = db.relationship('Reactives', backref='Реактив', lazy='dynamic')
        # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
        def __repr__(self):
            return '<Orders {}>'.format(self.order_date)








