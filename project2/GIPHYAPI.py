import os

#this will access the api key
GIPHY_API_KEY = os.environ.get("GIPHY_API_KEY")

if GIPHY_API_KEY is None:
    print("error... I don't think u set the api key")
else:
    def get_trending(api_key):
    url = "https://api.giphy.com/v1/gifs/trending?api_key={api_key}&limit=25&offset=0&rating=g"
    response = requests.get(url)
    # data = response.json(url)
    data = response.json()
    return data
   