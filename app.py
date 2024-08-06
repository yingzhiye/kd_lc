from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from waitress import serve
from database import db_session

from config import DevelopmentConfig,ProductionConfig
from models import KidneyCancer

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
def hello_world():  # put application's code here
    title = 'KDBioDB'
    title2 = 'An integrative multi-omics database on kidney disease!'
    return render_template('index.html', title = title, title2 = title2)

@app.route('/home/<string:input>')
def home_page():
    return f'Input {input}'

@app.route('/genomic_tbl.html')
def genomics_home():
    # 查询简单的表格过来
    aaa = db_session.query(KidneyCancer).all()
    return render_template('genomic_tbl.html')

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
    

# main
if __name__ == '__main__':
    if bDevelp:
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        serve(app, host='0.0.0.0', port=5000)
