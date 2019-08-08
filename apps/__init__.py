import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db =SQLAlchemy()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY = "dev",
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )
    if test_config is None:
        app.config.from_pyfile(os.path.join(app.instance_path,'config.py'),silent=False)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    from apps.auth_app.urls import auth_blueprint
    app.register_blueprint(auth_blueprint)
    return app

app = create_app()
@app.cli.command("init-db")
def create_inital_db():
    db.create_all()