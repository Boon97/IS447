<<<<<<< HEAD
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# initialise SQLAlchemy 
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECREY_KEY'] = 'top-sekrid'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
=======
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# initialise SQLAlchemy 
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECREY_KEY'] = 'top-sekrid'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
>>>>>>> c1daa13c026cdd946bd8e6e9a09f8e91c83910e4
