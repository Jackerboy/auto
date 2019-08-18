"""
===========================
File Name: __init__.py.py
Date: 2019/8/18
Software: PyCharm
Author: li_pin
===========================
"""
from flask_wtf import  FlaskForm
from wtforms import StringField,TextAreaField,IntegerField
from wtforms.validators import DataRequired,Length
from app.web.forms.validators import Unique
from app.web.models import ProjectInfo

class ProjectAddForm(FlaskForm):
    model_case = ProjectInfo
    project_name = StringField(label='项目名称',validators=[DataRequired(),Length(max=64,min=1),Unique(model_case,model_case.project_name)])
    simple_desc = TextAreaField(label='项目描述',validators=[Length(max=512,min=0)])



class ProjectDeleteForm(FlaskForm):
    id=IntegerField()