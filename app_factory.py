from flask import Flask
import settings  
from database import db
from blueprints.user.bp import init_app as user_init
from flask_cors import CORS


def create_app(default_settings=None):
    if default_settings == None:
        default_settings = settings
    app = Flask(__name__)
    app.config.from_object(default_settings)
    db.init_app(app)
    user_init(app)
    with app.app_context():
        db.create_all()
        db.session.commit()
    CORS(app)
    return app


