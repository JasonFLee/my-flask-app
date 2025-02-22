from flask import Flask, jsonify
from thingsNearMe import get_hidden_gems, get_atlas_obscura_places

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Hidden Gems API!"})

@app.route("/api/get-hidden-gems")
def api_hidden_gems():
    return jsonify({"places": get_hidden_gems()})

@app.route("/api/get-atlas-obscura")
def api_atlas_obscura():
    return jsonify({"places": get_atlas_obscura_places()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
