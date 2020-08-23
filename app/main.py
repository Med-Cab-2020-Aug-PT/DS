from flask import Flask, jsonify
from data.mongo import DB

API = Flask(__name__)

@API.route("/")
def index():
    return jsonify("API Online!")


@API.route("/recommendations/<user_input>", methods=['GET'] )
def recommendations():
    rec_strains = x
    return jsonify(rec_strains)


@API.route("/treats")
def treats():
    return jsonify("API Online!")


if __name__ == '__main__':
    API.run(debug=True)
