from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager

app=Flask(__name__)
app.config['SECRET_KEY']='e39d2399f9f1f1e0cf1d078b861b370d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'                                                                            
db = SQLAlchemy(app)
bcrypt = Bcrypt(app) 
login_manager = LoginManager(app)
login_manager.login_view= 'login' #tambahkan
login_manager.login_message_category = 'info'

from blog_ku import routes