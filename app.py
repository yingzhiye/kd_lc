from apps import create_app

app = create_app()

if __name__ == '__main__':
    print(app.static_folder)
    print(app.static_url_path)
    print(app.template_folder)
    app.run(port=8080)
