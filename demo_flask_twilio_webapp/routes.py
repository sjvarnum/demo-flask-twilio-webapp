from flask import Blueprint, render_template, request, flash, redirect, url_for


bp = Blueprint('/', __name__, url_prefix='/')

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')