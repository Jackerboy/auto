from app.web import web
from flask import render_template
from app.web.models import ProjectInfo

@web.route('/')
def index():
    projects = ProjectInfo.all()
    print(projects)

    return render_template('index.html',projects = projects)