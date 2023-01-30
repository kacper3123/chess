from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_socketio import SocketIO
from flask_session import Session
from app_import import create_app

app = Flask(__name__)
app.config.from_object(Config)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SECRET_KEY'] = 'key'
app.secret_key = 'key'
app.debug = True
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
db = SQLAlchemy(app)
session = Session()
session.init_app(app)
migrate = Migrate(app, db)
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins=[
                  'http://127.0.0.1:5000', 'http://localhost:5000'])

from app import models, events, routes