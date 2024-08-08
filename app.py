from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from waitress import serve
from database import db_session, mdGenomics, mdtransGene, mdtransRelated
from config import DevelopmentConfig,ProductionConfig
from models import *

# 开发模式标识符
bDevelp = True

app = Flask(__name__)

# 选择配置
if bDevelp:
    app.config.from_object(DevelopmentConfig())
else:
    app.config.from_object(ProductionConfig())

# 配置使用
# print(app.config)
# print(app.config['SECRET_KEY'])

# 扩展注册区域
Bootstrap(app)

'''视图区域，在这里实现视图编码'''
@app.route('/')
def home_page():  # put application's code here
    # title = 'An integrative multi-omics database on kidney disease'
    return render_template('index.html')

@app.route('/genomic.html')
def genomics_home():
    # 查询简单的表格过来, 展示的内容在后端进行处理
    seq = db_session.query(genomicModel).all()
    seq[1].metadata.tables['genomics_gwsall'].c[0].name
    tables = mdGenomics.c  # tables[].name 是表头名
    
    return render_template('genomic.html', datas = seq)

@app.route('/transcriptome.html')
def transcriptome_home():
    # 查询简单的表格过来, 展示的内容在后端进行处理
    seqGene = db_session.query(GeneTranModel).all()
    seqRelated = db_session.query(RelatedTranModel).all()
    tablesGene = mdtransGene.c  # tables[].name 是表头名
    tablesRelated = mdtransRelated.c  # tables[].name 是表头名
    return render_template('transcriptome.html', datas = seqGene, datas1 = seqRelated)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
    

# main
if __name__ == '__main__':
    if bDevelp:
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        serve(app, host='0.0.0.0', port=5000)
