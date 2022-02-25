from flask import Flask
from ..models import app
# from ..managers import user_manager
# from flask import render_template
# import os
# CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
# _CURRENT_DIR = os.path.dirname(os.path.abspath(CURRENT_DIR))
# __CURRENT_DIR = os.path.dirname(os.path.abspath(_CURRENT_DIR))
# path = os.path.join(__CURRENT_DIR)


# @app.route('/welcome', methods=['GET'])
# def home():
#     return render_template(path, name_recover = _welcome())

@app.route('/test')
def test():
    return "hello"
