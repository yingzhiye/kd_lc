# 反射得到orm
from sqlalchemy.orm import Session

from apps import metaBase, engine

def getGenomicsObj():
    genomics_info = metaBase.classes.genomics_gwsall
    ## select * from table11
    dataAll = session.query(genomics_info).all()
    print(dataAll)
    return genomics_info
