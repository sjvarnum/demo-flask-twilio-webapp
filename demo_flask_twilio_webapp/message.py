import os, sys, time

import psycopg2
from psycopg2 import OperationalError, errorcodes, errors

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user

from werkzeug.security import generate_password_hash, check_password_hash

from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

from .models import User, Contact
from . import db


bp = Blueprint('message', __name__, url_prefix='/message')

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        sendto = request.form['sendto']

        ACCOUNT_SID = os.environ.get('TWILIO_TEST_ACCOUNT_SID')
        AUTH_TOKEN = os.environ.get('TWILIO_TEST_AUTH_TOKEN')        
        FROM_ = os.environ.get('TWILIO_TEST_FROM')

        client = Client(ACCOUNT_SID, AUTH_TOKEN)

        rows = list()
        if sendto == '1':
            for row in db.session.query(Contact.phone, Contact.name, Contact.notes):
                rows.append(row)

        elif sendto == '2':
            for row in db.session.query(Contact.phone, Contact.name, Contact.notes).filter(Contact.notes=='Tues-Thurs-Class'):
                rows.append(row)

        elif sendto == '3':
            for row in db.session.query(Contact.phone, Contact.name, Contact.notes).filter(Contact.notes=='Wed-Fri-Class'):
                rows.append(row)

        for phone, name, notes in rows:
            phone = f'+1{phone}'
            name = name
            try:
                message = client.messages.create(
                    body=f'{title}: {body}',
                    from_=FROM_,
                    to=phone
                    )
                flash(f'Message sent to {name}: {phone}', 'info')
            except TwilioRestException as e:
                error_status = e.status
                error_msg = e.msg
                flash(f'Could not send message. {error_msg}', 'danger')
        return redirect(url_for('message.create'))

    return render_template('message/create.html')