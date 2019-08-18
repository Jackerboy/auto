from app.web import web
from flask import render_template

@web.route('/list_suites')
def list_suites():
    return 'ceses'


@web.route('/suites')
def suites():
    return 'ceses'

@web.route('/create_suite')
def create_suite():
    return 'projects'