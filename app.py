from flask_sqlalchemy import SQLAlchemy

from apps import create_app

app = create_app()


if __name__ == '__main__':
    print(app.static_folder)
    print(app.template_folder)
    app.run(port=8080)
