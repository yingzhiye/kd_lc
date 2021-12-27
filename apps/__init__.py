# 通过app工厂创建，将配置信息全部填过来，app.py只负责启动
from flask import Flask
from sqlalchemy.ext.automap import automap_base
from apps.genomics.view import genomics_bp
from config import DevelopmentConfig
from exts.database import initDBMeta

engine = None
metaBase = automap_base()
session = None


SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:3@10.91.221.46:5432/KidneyBioDB"

def create_app():
    app = Flask(__name__)  # app是一个核心对象
    app.config.from_object(DevelopmentConfig)
    # 蓝图是路由的另外一种表示方式
    app.register_blueprint(genomics_bp)  # 将app绑定到蓝图对象上
    # db.init_app(app)  # 不用这个db了
    initDBMeta(SQLALCHEMY_DATABASE_URI, engine, metaBase)
    # print(baseMeta)
    print(app.url_map)  # 打印app的路由

    return app
