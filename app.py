from flask import Flask, url_for, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from config import Config
from database import db_session


app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def hello_world():  # put application's code here
    title = 'KDBioDB'
    title2 = 'An integrative multi-omics database on kidney disease!'
    return render_template('index4.html', title = title, title2 = title2)

@app.route('/home/<string:input>')
def home_page():
    return f'Input {input}';

@app.route('/genomic_tbl.html')
def genomics_home():
    # 查询简单的表格过来
    db_session.query_property()
    return render_template('genomic_tbl.html', );

# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     db_session.remove()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
