from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from .models import User, Contact
from . import db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('add-user', methods=['GET', 'POST'])
@login_required
def add_user():
    if request.method == 'POST':
        name = request.form.get('name')
        email =  request.form.get('email').lower()
        password = request.form.get('password')

        check_email = User.query.filter_by(email=email).first()

        if check_email:
            error = f'User {email} already exists.'
            flash(error, 'danger')
        else:
            new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('User added successfully!', 'success')
            return redirect(url_for('auth.login'))

    return render_template('auth/add-user.html')


@bp.route('add-contact', methods=['GET', 'POST'])
@login_required
def add_contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email').lower()
        phone = request.form.get('phone')

        check_email = Contact.query.filter_by(email=email).first()

        if check_email:
            error = f'Contact {email} already exists.'
            flash(error, 'danger')
        else:
            new_user = Contact(email=email, name=name, phone=phone)
            db.session.add(new_user)
            db.session.commit()
            flash('Contact added successfully!', 'success')
            return redirect(url_for('auth.add_contact'))

    return render_template('auth/add-contact.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        error = None
        
        user = User.query.filter_by(email=email).first()
        if user is None:
            error = 'Incorrect email.'
        elif not check_password_hash(user.password, password):
            error = 'Incorrect password.'

        if error is None:
            flash('Logged in successfully!', 'success')
            login_user(user, remember=True)
            return redirect(url_for('message.create'))

        flash(error, 'danger')

    return render_template('auth/login.html', user=current_user)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
