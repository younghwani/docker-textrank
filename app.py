from flask import Flask, jsonify, request
from summary import summary_content

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'


@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.args.get('text')
    summary = summary_content(text)
    return jsonify(summary)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
