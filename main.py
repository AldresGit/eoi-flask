from flask import Flask, request
from flask.json import jsonify

from .services import UserService

app = Flask(__name__)

@app.route('/api/v1/users')
def get_user_list():
    return jsonify([
        {'username': 'alberto'},
        {'username': 'javi'},
        {'username': 'manolo'},
    ])

@app.route('/api/v1/users', methods=['POST'])
def create_user():
    # user = UserService.create(user_data)
    user = {'username': 'javi'}
    return jsonify(user)

@app.route('/api/v1/users/<user_id>')
def get_user(user_id):
    # user = UserService.retrieve(user_id)
    user = {'username': 'javi'}
    return jsonify(user)

@app.route('/api/v1/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    # user = UserService.update(user_id, request.json)
    user = {'username': 'javi'}
    return jsonify(user)

@app.route('/api/v1/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    # user = UserService.delete(user_id)
    return '', 204

@app.route('/api/v1/posts')
def get_post_list():
    return jsonify([
        {'title': 'Mi titulo 1'},
        {'title': 'Mi titulo 2'},
        {'title': 'Mi titulo 3'},
    ])