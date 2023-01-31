from app_import import create_app
from flask_socketio import SocketIO
from gevent.pywsgi import WSGIServer
from gevent.monkey import patch_all

app = create_app()

from app import models, routes, events

if __name__ == "__main__":
    socketio = SocketIO(app)
    socketio.init_app(app, cors_allowed_origins=['http://127.0.0.1:5000', 'http://localhost:5000'])
    socketio.run(app, host="http://127.0.0.1:5000", debug=True)
    patch_all()
