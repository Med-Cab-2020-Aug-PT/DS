from flask import Flask, jsonify

API = Flask(__name__)

@API.route("/")
def index():
    return jsonify("Welcome to Med Cabinet Strain Recommendation API!")


@API.route("/recommendations/<user_input>", methods=['GET'] )
def recommendations():
    rec_strains = _##TODO
    return jsonify(rec_strains)


@API.route("/treats")
def treats():
    return jsonify("API Online!")


if __name__ == '__main__':
    API.run(debug=True)
