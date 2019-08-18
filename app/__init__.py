"""初始化app核心对象
配置相关插件

"""
from flask import Flask
from flask_migrate import Migrate

from app.config import config,DevelopmentConfig,ProdConfig,TestConfig
from app.web.models import db
from app.web.template_env import str_time

app = Flask(__name__)

migrate = Migrate()
migrate.init_app(app,db)



#其他的初始化对象

def create_app():
    """初始化"""
    app.config.from_object(config)
    # 初始化数据库
    db.init_app(app)

    # 配置文件
    # 自定义的错误处理机制
    # 模板过滤器注册

    # 注册蓝图
    from app.web import web
    app.register_blueprint(web)

    #添加过滤器
    app.add_template_filter(str_time)
    return app