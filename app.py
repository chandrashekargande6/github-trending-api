from flask import Flask, jsonify
from scraper import fetch_trending_repos

app = Flask(__name__)

@app.route("/api/github/trending", methods=["GET"])
def get_trending_repos():
    try:
        data = fetch_trending_repos()
        return jsonify({"success": True, "data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)