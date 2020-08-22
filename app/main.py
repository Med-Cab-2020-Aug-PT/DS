from flask import Flask, jsonify


API = Flask(__name__)

@API.route("/")
def index():
    return jsonify("API Online!")



if __name__ == '__main__':
    API.run(debug=True)