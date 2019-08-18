from app.web import web
from flask import render_template

@web.route('/list_ceses')
def list_cases():
    return 'ceses'

@web.route('/create_case')
def create_case():
    return 'projects'