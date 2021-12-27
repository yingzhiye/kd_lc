from flask import Blueprint, render_template

from apps.database import DBglobal

genomics_bp = Blueprint('genomics', __name__)
genomicInfo = None
db_session = None


@genomics_bp.before_app_first_request
def setup():
    global genomicInfo, db_session
    genomicInfo = DBglobal.metaBase.classes.genomics_gwsall
    db_session = DBglobal.db_session
    # print(genomicInfo)

@genomics_bp.route('/genomic_tbl.html')
def genomics_index():
    # 查询简单的表格过来
    labels = db_session.query(genomicInfo).selectable.columns
    datas = db_session.query(genomicInfo).all()
    # print(labels)
    # print(datas)
    return render_template('genomic_tbl.html', datas=datas)


@genomics_bp.route('/serach', methods=['GET', 'PUT'])
def genomics_search():
    return '补充查询form的html'

