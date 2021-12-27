from flask import Blueprint, render_template
from sqlalchemy.orm import Session

from apps.genomics.models import getGenomicsObj

genomics_bp = Blueprint('genomics', __name__)


# 首页临时放到这里来
@genomics_bp.route('/')
def hello_world():  # put application's code here
    title = 'KDBioDB'
    title2 = 'An integrative multi-omics database on kidney disease!'
    return render_template('index4.html', title=title, title2=title2)


@genomics_bp.route('/genomics')
def genomics_index():
    # 查询简单的表格过来

    return render_template('genomic_tbl.html', )


@genomics_bp.route('/serach', methods=['GET', 'PUT'])
def genomics_search():
    return '补充查询form的html'
