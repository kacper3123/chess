from flask import Flask
from flask_session import Session
from flask_socketio import SocketIO
from app import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    app.config['SECRET_KEY'] = 'key'
    app.secret_key = 'key'
    app.debug = True
    session = Session()
    session.init_app(app)

    from app import routes, models, events
    return app