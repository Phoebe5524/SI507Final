# datastructure.py
import os
import json
import requests

class ArtistData:
    def __init__(self, api_key, base_url, cache_folder):
        self.API_KEY = api_key
        self.BASE_URL = base_url
        self.CACHE_FOLDER = cache_folder

    def fetch_similar_artists(self, artist):
        params = {
            "method": "artist.getsimilar",
            "artist": artist,
            "api_key": self.API_KEY,
            "format": "json",
            "limit": 20,
        }
        response = requests.get(self.BASE_URL, params=params)
        return response.json()

    def cache_similar_artists(self, artist, data):
        filename = f"{self.CACHE_FOLDER}/{artist.lower().replace(' ', '_')}.json"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            json.dump(data, f)

    def load_cached_similar_artists(self, artist):
        filename = f"{self.CACHE_FOLDER}/{artist.lower().replace(' ', '_')}.json"
        if os.path.exists(filename):
            with open(filename, "r") as f:
                return json.load(f)
        else:
            return None
