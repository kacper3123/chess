from flask import flash, render_template, redirect, url_for
from app import app, db



@app.route('/')
def index():
    return render_template('base.html')