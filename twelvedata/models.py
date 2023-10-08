from werkzeug.security import generate_password_hash 
from flask_sqlalchemy import SQLAlchemy 
from flask_login import UserMixin, LoginManager 
from datetime import datetime
import uuid

db = SQLAlchemy() 
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id) 


watchlist= db.Table(
    "watchlist", 
    db.Column("user_id", db.String, db.ForeignKey("user.user_id"), nullable=False),
    db.Column("stock_id", db.String, db.ForeignKey("stock_data.stock_id"), nullable=False)
)


class User(db.Model, UserMixin):


    user_id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    username = db.Column(db.String(30), nullable=False, unique = True)
    email = db.Column(db.String(150), nullable = False, unique = True)
    password = db.Column(db.String, nullable=False)
    date_added = db.Column(db.DateTime, default = datetime.utcnow)

    watchlist= db.relationship("StockData", secondary= "watchlist", backref=db.backref("watching"))

    def __init__(self, first_name, last_name, username, email, password):
        self.user_id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password
        


    def set_id(self):
        return str(uuid.uuid4())
    
    def add_to_watchlist(self, name):
        self.watchlist.append(name) 
        db.session.commit()


class StockData(db.Model):

    stock_name = db.Column(db.String(30))
    stock_ticker = db.Column(db.String(5))
    stock_id = db.Column(db.String, primary_key = True)
    current_date = db.Column(db.DateTime, default = datetime.utcnow)
    open_price = db.Column(db.Numeric(10))
    close_price = db.Column(db.Numeric(10))
    volume = db.Column(db.Numeric(15))

    def __init__(self, stock_name, stock_ticker, open_price, close_price, volume):
        self.stock_id = self.set_id()
        self.stock_name = stock_name
        self.stock_ticker= stock_ticker
        self.open_price= open_price
        self.close_price= close_price
        self.volume = volume
    
    def set_id(self):
        return str(uuid.uuid4())


    
    