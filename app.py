from flask import Flask, jsonify, request
from flask_cors import CORS
from sqlalchemy import true
app = Flask(__name__)
CORS(app)
incomes = [
    {'description': 'salary', 'amount': 5000}
]


@app.route("/")
def greeting():
    return jsonify(incomes)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=true)
