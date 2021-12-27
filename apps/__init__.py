# 通过app工厂创建，将配置信息全部填过来，app.py只负责启动
from flask import Flask, render_template
from apps.genomics.view import genomics_bp
from config import DevelopmentConfig
from apps.database import initDBMeta

SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:3@10.91.221.46:5432/KidneyBioDB"

def create_app():
    app = Flask(__name__)  # app是一个核心对象
    app.config.from_object(DevelopmentConfig)
    # 蓝图是路由的另外一种表示方式
    app.register_blueprint(genomics_bp)  # 将app绑定到蓝图对象上
    initDBMeta(SQLALCHEMY_DATABASE_URI)
    # print(baseMeta)
    print(app.url_map)  # 打印app的路由

    return app


