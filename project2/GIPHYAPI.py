import os
import requests

API_KEY = os.environ["GIPHY_API_KEY"]
print(API_KEY)

class GiphyAPI:
    def __init__(self):
        self.api_key = API_KEY  

    def get_trending(self):
        url = f"https://api.giphy.com/v1/gifs/trending?api_key={self.api_key}&offset=0&rating=g"
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()
        return data["data"]

    def search(self, query):
        url = f"https://api.giphy.com/v1/gifs/search?api_key={self.api_key}&q={query}&offset=0&rating=g&lang=en"
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        return data["data"]