from flask import Flask, jsonify
from lib.rot import Rot

app = Flask(__name__)


@app.route('/')
def index():
    return 'ROT26!'


@app.route('/api/rot26/<string>', methods=['GET'])
def rot26(string = ""):
    rot = Rot()

    result = rot.rot26(string)

    return jsonify(result)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
