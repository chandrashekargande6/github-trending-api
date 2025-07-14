from flask import Flask, jsonify
from scraper import fetch_trending_repos  # Your scraper function
import os

app = Flask(__name__)

@app.route('/api/github/trending', methods=['GET'])
def get_trending():
    try:
        data = fetch_trending_repos()
        return jsonify({"success": True, "data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    # Use PORT from environment if available (e.g. Render), else default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
