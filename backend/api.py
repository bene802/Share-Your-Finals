from flask import Flask, request, jsonify, make_response
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = '6f5029c57a0d0b5a688700d3d3675d5e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


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
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date}')"


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


@app.route('/post/update', methods=['POST'])
def update_user_post():
    try:
        data = request.get_json()
        post = Post.query.filter_by(id=data['id']).first()
        if not post:
            return jsonify({'message': 'Failed, post not exists'}), 400
        if data['user_id'] != post.user_id:
            return jsonify({'message': 'No access'}), 400
        post.title = data['title']
        post.content = data['content']
        db.session.commit()
        return jsonify({'message': 'Updated successfully'}), 200
    except:
        return jsonify({'message': 'Invalid Request'}), 400


@app.route('/post/delete/<post_id>', methods=['DELETE'])
def delete_user_post(post_id):
    post = Post.query.get(post_id)
    if not post:
        return jsonify({'message': 'Failed, post not exists'}), 400
    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': 'Deleted successfully'}), 200


@app.route('/newPost', methods=["POST"])
def create_new_post():
    try:
        data = request.get_json()
        if not data['title'] or not data['content'] or not data['user_id']:
            return jsonify({'message': 'Invalid Request'}), 400
        post = Post(title=data['title'], content=data['content'], user_id=data['user_id'])
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
        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        user = User(username=data['username'], password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'New user created!'}), 200
    except:
        return jsonify({'message': 'Invalid Request'}), 400


if __name__ == '__main__':
    app.run(debug=True)
