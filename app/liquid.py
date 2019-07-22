from flask import jsonify, request

from app.settings import app
from app.db import User


def home():
    if request.method == 'GET':
        return jsonify({'message': 'Hello, GET!'})
    elif request.method == 'POST':
        return jsonify({'message': 'Hello, POST!'})
