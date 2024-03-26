# import requests

# def get_trending(api_key):
#     url = "https://api.giphy.com/v1/gifs/trending?api_key={api_key}&limit=25&offset=0&rating=g"
#     response = requests.get(url)
#     data = response.json()
#     return data

# if __name__ == "__main__":
#     api_key = "ZYdJkh7f8h7myXG5gfjUd3jZT1BoshEo"
#     gifs = get_trending(api_key)
#     print (gifs)

#     #this is the "quick and dirty.py"

import os
import requests

def get_trending(api_key):
    url = "https://api.giphy.com/v1/gifs/trending?api_key={api_key}&limit=25&offset=0&rating=g"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    api_key = os.environ.get("GIPHY_API_KEY")

    if not api_key:
        print("Error....check your api key")
    else:
        gifs = get_trending(api_key)
        print(gifs)

