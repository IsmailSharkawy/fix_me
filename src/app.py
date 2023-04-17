import requests
from flask import Flask, jsonify, request
from flask_caching import Cache 

app = Flask(__name__)
app.config.from_object('config.Config')
cache = Cache(app)
cache.set("call", "red")


@app.route("/universities")
def get_universities():
    if cache.get("call"):
        API_URL = "http://universities.hipolabs.com/search?country="
        search = request.args('country')
        r = requests.get(f"{API_URL}{search}")
        return jsonify(r.json())
    else:
        return {"Error":"Cache isn't working"} 

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5656)
