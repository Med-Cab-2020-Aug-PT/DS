from flask import Flask, jsonify

API = Flask(__name__)

@API.route("/")
def index():
    return jsonify("Welcome to Med Cabinet Strain Recommendation API!")


@API.route("/recommendations/<user_input>", methods=['GET'] )
def recommendations(user_input):
    rec_strains = PredictionBot()
    return jsonify(rec_strains.predict(user_input))


if __name__ == '__main__':
    API.run(debug=True)
