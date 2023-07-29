from flask import Flask, jsonify

app = Flask(__name__)


@app.config('/')
def home():
    return jsonify({'message':'This is a sample text'})