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
baseMeta = automap_base()
engine = None

# 存储一些配置
class DBMetaObj():
    def __init__(self, engine, session, baseMeta):
        self.engine = engine
        self.session = session
        self.baseMeta = baseMeta




def initDBMeta(uri):
    # 创建数据库连接
    engine = create_engine(uri)

    # 使用普通模式反射表对象
    # metadata = MetaData()
    # metadata.reflect(band=engine)

    # 使用ORM反射表对象
    baseMeta.prepare(engine, reflect=True)
    keys = baseMeta.classes.keys()
    print(keys)

    # genomics的
    genomics_info = baseMeta.classes.genomics_gwsall
    session = Session(bind=engine)

