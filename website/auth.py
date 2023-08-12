# authentication

from flask import Blueprint, request, flash, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET", "POST"])
def login():
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return '<p>Logged out</p>'

@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 7:
            flash('Email has to be longer than 7 characters.', category='error')
        elif len(firstName) < 2:
            flash('Name has to be longer than 2 characters.', category='error')
        elif len(password1) < 5:
            flash('Password has to be longer than 5 characters.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category="error")
        else:
            flash('Account created', category="success")
    return render_template("signup.html", boolean=True)