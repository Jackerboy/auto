from app.web import web
from flask import render_template

@web.route('/list_modules')
def list_modules():
    return 'models'


@web.route('/create_module')
def create_module():
    return 'projects'