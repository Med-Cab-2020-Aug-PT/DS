from flask import Flask, jsonify
from app.model import PredictionBot

API = Flask(__name__)

@API.route("/")
def index():
    return jsonify("Welcome to Med Cabinet Strain Recommendation API!")


@API.route("/recommendations/<user_input>")
def recommendations(user_input):
    conoissieur = PredictionBot()
    rec_strains = conoissieur.predict(user_input)
    return jsonify(rec_strains)


if __name__ == '__main__':
    API.run(debug=True)
