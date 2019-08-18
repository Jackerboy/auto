import time

from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

from app.errors.exceptions import DatabaseException

db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer,primary_key=True)
    created_at = db.Column(db.Integer,default=int(time.time()))
    updated = db.Column(db.Integer,default=int(time.time()),onupdate=int(time.time()))
    status = db.Column(db.SmallInteger,default=1)

    @classmethod
    def all(cls):
        return cls.query.order_by(desc(cls.updated)).all()


    @classmethod
    def paginate(cls,page):
        """分页器"""
        return cls.query.paginate(page=int(page),per_page=current_app.config['PER_PAGE'])



class User(Base):
    # __table__ = 'user'
    name = db.Column(db.String(32),nullable=False,default='',unique=True)



class ProjectInfo(Base):
    project_name = db.Column(db.String(32), nullable=False, default='', unique=True)
    simple_desc = db.Column(db.String(500), nullable=False, default='')
    DELETE_STATUS = 0


    @classmethod
    def insert(cls,data):
        """添加新的项目
        例子：data:{'project_name':'sf','simple_desc':'sf'}
        """
        project = ProjectInfo(
            project_name=data.get('project_name',''),
            simple_desc=data.get('simple_desc','')
        )
        try:
            db.session.add(project)
            db.session.commit()
            return project
        except Exception as e:
            #logger
            current_app.logger.error('project 保存出错')
            # db.session.roolbaclk()
            # 抛出异常
            return DatabaseException('project 数据异常')


    def update(self,data):
        """更新项目
        例子：data:{'project_name':'sf','simple_desc':'sf'}
        """
        self.project_name =data.get('project_name','')
        self.simple_desc = data.get('simple_desc','')
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except Exception as e:
            #logger
            current_app.logger.error('project 更新出错')
            # db.session.roolbaclk()
            # 抛出异常
            return DatabaseException('project 数据异常')


    def delete(self):
        """删除记录
        bug:
        1.项目还会展示
        3.module，case还会展示？
        """
        self.status = self.DELETE_STATUS
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except Exception as e:

            current_app.logger.error('project 更新出错')
            return DatabaseException('project 数据异常')
