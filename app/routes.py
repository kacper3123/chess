from flask import flash, render_template, redirect, url_for, session
from app import app, db
from app.models import User
from app.forms import LoginForm, RoomForm, RegisterForm
from flask_login import current_user, login_user, logout_user, login_required


@app.route('/', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('chat'))
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))

        login_user(user, remember=form.remember_me.data)
        session['name'] = user.name
        return redirect(url_for('chat'))

    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username
        email = form.email
        form.validate_email(email)
        form.validate_username(username)
        user = User(username.data, username.data, email.data)

        user.set_password(form.password.data)

        try:
            db.session.add(user)
            db.session.commit()
                        
            login_user(user)
            session['name'] = username.data
            return redirect(url_for('chat'))
        except Exception as e:
            db_error = e
            return render_template('register.html', title="Register", form=form, db_error=db_error)



    return render_template('register.html', title="Register", form=form)


@login_required
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    form = RoomForm()
    if form.validate_on_submit():
        session['room'] = f"{form.room.data}"
        return render_template('chat.html', session=session)
    return render_template('chatform.html', session=session, form=form)


@login_required
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))
