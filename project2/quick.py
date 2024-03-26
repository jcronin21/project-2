import requests

def get_trending(api_key):
    url = "https://api.giphy.com/v1/gifs/trending?api_key={api_key}&limit=25&offset=0&rating=g"
    response = requests.get(url)
    # data = response.json(url)
    data = response.json()
    return data

if __name__ == "__main__":
    api_key = "1rcKChP84QC5RgzDuP3UyFzz79uPXwym"
    gifs = get_trending(api_key)
    print (gifs)