'''
Example imports:
from datetime import datetime, timedelta, timezone, time
from flask import render_template,redirect,url_for, request, make_response
from flask_login import login_required, current_user

from . import sample_bp

'''

'''
@sample_bp.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')
'''