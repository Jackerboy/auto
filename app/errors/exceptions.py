"""
===========================
File Name: exceptions.py
Date: 2019/8/18
Software: PyCharm
Author: li_pin
===========================
"""

class DatabaseException(Exception):
    """数据库错误"""
    pass


class ValidationException(Exception):
    """验证异常"""
    pass