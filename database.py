from sqlalchemy import create_engine, MetaData
import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

from config import DevelopmentConfig, ProductionConfig

# TODO: Change to 可配置的数据库连接
# engine = create_engine("postgresql://postgres:3@10.91.221.46:5432/KidneyBioDB")
# engine = create_engine(ProductionConfig().SQLALCHEMY_DATABASE_URI)
engine = create_engine(DevelopmentConfig().SQLALCHEMY_DATABASE_URI)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


md = MetaData() # 元数据,用于获取表头等信息
mdGenomics = sqlalchemy.Table('show_genomics_gwsall', md, autoload_with=engine)
mdtransGene = sqlalchemy.Table('show_gene_tran', md, autoload_with=engine)
mdtransRelated = sqlalchemy.Table('show_related_tran', md, autoload_with=engine)

def init_db():
    # 在这里导入定义模型所需要的所有模块，这样它们就会正确的注册在
    # 元数据上。否则你就必须在调用 init_db() 之前导入它们。
    import models 
    # Base.metadata.create_all(bind=engine)


 
 