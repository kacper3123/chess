from flask import flash, render_template
from app import app

@app.route('/')
def index():
    return render_template('chess.html')