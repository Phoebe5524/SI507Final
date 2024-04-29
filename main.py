# main.py
from flask import Flask, render_template, request, jsonify
from DataStructure import ArtistData

app = Flask(__name__)

API_KEY = "b9c1f7ee94f6081127d354e0aea70578"
BASE_URL = "https://ws.audioscrobbler.com/2.0/"
CACHE_FOLDER = "cached_data"

artist_data = ArtistData(API_KEY, BASE_URL, CACHE_FOLDER)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["GET"])
def search():
    artist_name = request.args.get("artist")
    if not artist_name:
        return jsonify({"error": "Artist name is required"}), 400

    # Fetch similar artists
    similar_artists = artist_data.fetch_similar_artists(artist_name)

    if not similar_artists:
        return jsonify({"error": "Failed to fetch similar artists"}), 500

    # Cache the fetched data
    artist_data.cache_similar_artists(artist_name, similar_artists)

    return jsonify(similar_artists)


if __name__ == "__main__":
    app.run(debug=True)
