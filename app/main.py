from flask import Flask, jsonify, request
from app.model import PredictionBot

API = Flask(__name__)

@API.route("/")
def index():
    return jsonify("Welcome to Med Cabinet Strain Recommendation API!")


@API.route("/recommendations/web_input>")
def recommendations(web_input):
    user_input = request.args[web_input]
    conoissieur = PredictionBot()
    rec_strains = conoissieur.predict(user_input)
    return jsonify(rec_strains)


if __name__ == '__main__':
    API.run(debug=True)
