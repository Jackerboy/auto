"""
===========================
File Name: validators.py
Date: 2019/8/18
Software: PyCharm
Author: li_pin
===========================
"""
from wtforms import ValidationError


class Unique:
    """验证器，验证某个模型某个字段是否在数据库里存在
    实例： Unique(Project，project,project_name)

    """

    def __init__(self,db_class,db_column,msg=None):

        self.db_class = db_class
        self.db_column = db_column

        self.msg = '数据库已存在' if msg is None else msg


    def __call__(self,form,field):

        res = self.db_class.query.filter(self.db_column == field.data).first()

        if res:
            raise ValidationError(self.msg)

        return res