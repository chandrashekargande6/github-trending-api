from flask import Flask, jsonify
from scraper import fetch_trending_repos
import os

app = Flask(__name__)

# ✅ New: Root route for welcome message
@app.route('/')
def home():
    return '''
    <h2>👋 Welcome to GitHub Trending API</h2>
    <p>To view trending repositories, go to:</p>
    <a href="/api/github/trending">/api/github/trending</a>
    '''

# ✅ API route for trending repos
@app.route('/api/github/trending', methods=['GET'])
def get_trending():
    try:
        data = fetch_trending_repos()
        return jsonify({"success": True, "data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# ✅ Bind to correct host and port for Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
