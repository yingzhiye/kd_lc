from flask import g
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

'''
在这里做所有数据库对象反射的配置，具体表的反射在各app的models里
'''

# 表名列表
# dialect+driver://username:password@host:port/database
# eg: psycopg2: engine = create_engine('postgresql+psycopg2://scott:tiger@localhost/mydatabase')

GENOMICS_TBLNAME = 'genomics_gwsall'


class DBglobal:
    db_session = None
    metaBase = None


def initDBMeta(uri):
    # 创建数据库连接
    engine = create_engine(uri)
    DBglobal.metaBase = automap_base()
    # 使用ORM反射表对象
    DBglobal.metaBase.prepare(engine, reflect=True)
    DBglobal.db_session = Session(bind=engine)




