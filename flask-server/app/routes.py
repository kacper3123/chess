from flask import flash, render_template, redirect, url_for
from app import app, db

@app.route('/board')
def index():
    return render_template('chess.html')