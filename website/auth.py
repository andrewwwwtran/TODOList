# authentication

from flask_login import login_user,login_required, logout_user, current_user
from . import db
from flask import Blueprint, request, flash, render_template, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # check if user exists
        user = User.query.filter_by(email = email).first()
        if user:
            # check password
            if check_password_hash(user.password, password):
                # log user in 
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Password is incorrect, try again.', category='error')
        else:
            flash('Email doesn\'t exist.', category='error')

    return render_template("login.html", user = current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email = email).first()

        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 7:
            flash('Email has to be longer than 6 characters.', category='error')
        elif len(firstName) < 2:
            flash('Name has to be longer than 1 characters.', category='error')
        elif len(password1) < 5:
            flash('Password has to be longer than 4 characters.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category="error")
        else:
            # create a new user
            newUser = User(email = email, firstName = firstName, password = generate_password_hash(password1, method='sha256'))
            db.session.add(newUser)
            db.session.commit()
            flash('Account created', category="success")
            return redirect(url_for('views.home'))
    return render_template("signup.html", user = current_user)