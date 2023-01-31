from flask import flash, render_template, redirect, url_for
from app import app, db



@app.route('/members')
def index():
    # return render_template('chess.html')
    return {"members": ["kacpi", "kacpi2", "kacpi3"]}