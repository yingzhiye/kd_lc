from flask import render_template

from apps import create_app
from apps.database import DBglobal

app = create_app()


# 首页临时放到这里来
@app.route('/')
def hello_world():  # put application's code here
    title = 'KDBioDB'
    title2 = 'An integrative multi-omics database on kidney disease!'
    return render_template('index4.html', title=title, title2=title2)

# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     DBglobal.db_session.remove()


if __name__ == '__main__':
    print(app.static_folder)
    print(app.template_folder)
    app.run(port=8080)
