from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import jwt
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = '6f5029c57a0d0b5a688700d3d3675d5e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date}')"


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(id=data['id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated


@app.route('/posts', methods=['GET'])
def get_all_posts():
    posts = Post.query.order_by(Post.date.desc())
    outputs = []
    for post in posts:
        output = {}
        output['id'] = post.id
        output['user_id'] = post.user_id
        output['title'] = post.title
        output['data'] = post.date
        output['content'] = post.content
        outputs.append(output)
    return jsonify({'posts': outputs}), 200


@app.route('/user/<user_id>', methods=['GET'])
def get_user_posts(user_id):
    posts = Post.query.filter_by(user_id=user_id).order_by(Post.date.desc())
    outputs = []
    for post in posts:
        output = {}
        output['id'] = post.id
        output['user_id'] = post.user_id
        output['title'] = post.title
        output['data'] = post.date
        output['content'] = post.content
        outputs.append(output)
    return jsonify({'posts': outputs}), 200


@app.route('/post/<post_id>/update', methods=['POST'])
@token_required
def update_user_post(current_user, post_id):
    try:
        data = request.get_json()
        post = Post.query.filter_by(id=post_id).first()
        if not post:
            return jsonify({'message': 'Failed, post not exists'}), 400
        if current_user.id != post.user_id:
            return jsonify({'message': 'No access'}), 401
        post.title = data['title']
        post.content = data['content']
        db.session.commit()
        return jsonify({'message': 'Updated successfully'}), 200
    except:
        return jsonify({'message': 'Invalid Request'}), 400


@app.route('/post/<post_id>/delete', methods=['DELETE'])
@token_required
def delete_user_post(current_user, post_id):
    post = Post.query.get(post_id)
    if current_user.id != post.user_id:
        return jsonify({'message': 'No access'}), 401
    if not post:
        return jsonify({'message': 'Failed, post not exists'}), 400
    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': 'Deleted successfully'}), 200


@app.route('/newPost', methods=["POST"])
@token_required
def create_new_post(current_user):
    try:
        data = request.get_json()
        if not data['title'] or not data['content']:
            return jsonify({'message': 'Invalid Request'}), 400
        post = Post(title=data['title'], content=data['content'], user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        return jsonify({'message': 'New post created!'}), 200
    except:
        return jsonify({'message': 'Invalid Request'}), 400


@app.route('/newUser', methods=['POST'])
def create_new_user():
    try:
        data = request.get_json()
        if not data['username'] or not data['password']:
            return jsonify({'message': 'Invalid Request'}), 400
        userExist = User.query.filter_by(username=data['username']).first()
        if userExist:
            return jsonify({'message': 'Username exsited! Please try a different username.'}), 400
        hashed_password = generate_password_hash(data['password'], method='sha256')
        user = User(username=data['username'], password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'New user created!'}), 200
    except:
        return jsonify({'message': 'Invalid Request'}), 400


@app.route('/login')
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    user = User.query.filter_by(username=auth.username).first()

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

        return jsonify({'token': token.decode('UTF-8')})

    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})


@app.route('/test', methods=['GET'])
def test():
    users = User.query.all()
    outputs = []
    for user in users:
        output = {}
        output['username'] = user.username
        output['password'] = user.password
        outputs.append(output)
    return jsonify({"users": outputs})
    # db.session.query(User).delete()
    # db.session.commit()
    # return ''


if __name__ == '__main__':
    app.run(debug=True)
