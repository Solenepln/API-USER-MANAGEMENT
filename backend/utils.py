from flask import Flask, redirect, url_for, session, request
from functools import wraps


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('username') is None:
            return redirect(url_for('login_user_login'))
        return f(*args, **kwargs)
    return decorated_function