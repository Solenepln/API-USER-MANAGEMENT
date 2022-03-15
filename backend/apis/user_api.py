from curses import flash
from functools import wraps
from flask import Flask, session, request, render_template, make_response, redirect, url_for
from flask_session import Session
from flask_restx import Namespace
from flask_restx import Api, Resource
from backend import app
from ..managers.user_manager import UserManager
import os
from ..utils import login_required
  
api = Namespace("users", description="user related")

# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if session.username is None:
#             return redirect(url_for('login', next=request.url))
#         return f(*args, **kwargs)
#     return decorated_function


@api.route("")
class UserApi(Resource):
    @login_required
    def get(self):
        #database with users
        users = UserManager.display_users()
        return make_response(render_template('users.html', users = users))

@api.route("/")
class InfosUser(Resource):
    def get(self):
        return make_response(render_template('user_info.html'))

@api.route('/<username>')
class InfosUserKnown(Resource):
    def get(self,username):
        if username:
            found_username = UserManager.info_user(username)  
        return make_response(render_template('user_info.html', found_username = found_username))
