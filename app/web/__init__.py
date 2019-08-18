from flask import Blueprint

web = Blueprint('web',__name__)



#路由
from .views import index,cases,models,projects,suites