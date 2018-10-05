from flask import Blueprint, request ,jsonify
from blueprints.user.model import User
from database import db
import json
from helpers.insertSQLintoList import insertSQLintoList as insertToList

bp = Blueprint('posts', __name__)


def init_app(app, url_prefix='/users'):
    app.register_blueprint(bp, url_prefix=url_prefix)

@bp.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        db.session.delete(User.query.filter(User.id==request.json.get('id')).one())
        db.session.commit()
        return 'ok'
    else:
        return 'Its only allowed POST method'

@bp.route('/register', methods=['POST'])
def new():
    if request.method == 'POST':
        username=request.json.get('username')
        password=request.json.get('password')
        email=request.json.get('email')
        user = User(username=username,email=email)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        return f'{user}'
    else:
        return 'Its only allowed POST method'

@bp.route('/verify', methods=['POST'])
def verify():
    if request.method == 'POST':
        username = request.json.get('username')
        user = User.query.filter_by(username = username).first()
        return f'{user}'
        



@bp.route('/', )
def list_posts():
    users = []
    insertToList(User,users)
    print(users)
    return f'{json.dumps(users)}'