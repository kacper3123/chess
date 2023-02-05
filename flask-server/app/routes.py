from flask import flash, render_template, redirect, url_for
from app import app, db

row_8 = [{"type": "r", "color": "b"}, {"type": "n", "color": "b"}, {"type": "b", "color": "b"}, {"type": "q", "color": "b"},
        {"type": "k", "color": "b"}, {"type": "b", "color": "b"}, {"type": "n", "color": "b"}, {"type": "r", "color": "b"}]

row_7 = [None, None, None, None, None, None, None, None]
row_6 = [None, None, None, None, None, None, None, None]
row_6 = [None, None, None, None, None, None, None, None]
row_4 = [None, None, None, None, None, None, None, None]
row_3 = [None, None, None, None, None, None, None, None]
row_2 = [None, None, None, None, None, None, None, None]

row_1 = [{"type": "r", "color": "w"}, {"type": "n", "color": "w"}, {"type": "b", "color": "w"}, {"type": "q", "color": "w"},
        {"type": "k", "color": "w"}, {"type": "b", "color": "w"}, {"type": "n", "color": "w"}, {"type": "r", "color": "w"}]
@app.route('/board')
def index():
    # return render_template('chess.html')
    return {"board": ["kacpi", "kacpi2", "kacpi3"]}