from sqlalchemy import create_engine
from sqlalchemy.orm import Session

'''
在这里做所有数据库对象反射的配置，具体表的反射在各app的models里
'''

# 表名列表
# dialect+driver://username:password@host:port/database
# eg: psycopg2: engine = create_engine('postgresql+psycopg2://scott:tiger@localhost/mydatabase')

GENOMICS_TBLNAME = 'genomics_gwsall'


def initDBMeta(uri, engine, metaBase):
    pass
    # 创建数据库连接
    engine = create_engine(uri)

    # 使用ORM反射表对象
    metaBase.prepare(engine, reflect=True)
    keys = metaBase.classes.keys()
    session = Session(bind=engine)
    print(keys)



