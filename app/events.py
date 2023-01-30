from flask import session
from app import socketio
from flask_socketio import emit, leave_room, join_room


@socketio.on('join', namespace='/chat')
def join(message):
    username = message['name']
    room = message['room']
    join_room(room)
    emit('status', {'msg': f'{username} has entered the room.'}, room=room, username=username)

@socketio.on('text', namespace='/chat')
def text(message):
    username = message['name']
    room = message['room']
    print(username)
    emit('message', {'msg': f'{message["msg"]}', 'username': f'{username}'}, room=room, username=username)

@socketio.on('left', namespace='/chat')
def left(message):
    username = message['name']
    room = message['room']
    leave_room(room)
    session.clear()
    emit('status', {'msg': f'{username} has left the room.'}, room=room, username=username)

