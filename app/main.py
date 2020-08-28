from flask import Flask, jsonify, request, make_response
from app.model import PredictionBot

from app.model import PredictionBot

API = Flask(__name__)

<<<<<<< HEAD
=======
#CORS requirement to access apis - (Courtesy-Jisha)
@API.route.before_request
def before_request():
    """ CORS preflight, required for off-server access """

    def _build_cors_prelight_response():
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "*")
        response.headers.add("Access-Control-Allow-Methods", "*")
        return response

    if request.method == "OPTIONS":
        return _build_cors_prelight_response()

@API.route.after_request
def after_request(response):
    """ CORS headers, required for off-server access """
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response
>>>>>>> eed51c2653fcc630efa21057653878b3edae498b

@API.route("/")
def index():
    return jsonify("Welcome to Med Cabinet Strain Recommendation API!")


<<<<<<< HEAD
@API.route("/recommendations/<user_input>", methods=['GET'])
def recommendations(user_input):
    rec_strains = PredictionBot()
    return jsonify(rec_strains.predict(user_input))
=======
@API.route("/recommendations/<web_input>")
def recommendations(web_input):
    connoissieur = PredictionBot()
    rec_strains = connoissieur.predict(user_input)
    return jsonify(rec_strains)
>>>>>>> eed51c2653fcc630efa21057653878b3edae498b


if __name__ == '__main__':
    API.run(debug=True)
