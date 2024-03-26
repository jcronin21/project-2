import unittest
from ..GIPHYAPI import GiphyAPI


class TestGiphyAPI(unittest.TestCase):
     def testing(self):
        self.giphy_api = GiphyAPI()

def test_get_trending(self):
    trending_giphy = self.giphy_api_get_trending()

    self.assertTrue(len(trending_giphy)>0)
    for gif in trending_giphy:
        self.assertIn("title",gif)
        self.assertIn("url",gif)

    # search_for = ["title,url"] 
def test_search(self):
    query = "cats"
    searchresult = self.giphy_api.search(query)

    self.assertTrue(len(searchresult)>0)
    for gif in searchresult:
        self.assertIn("title",gif)
        self.assertIn("url",gif)

        #chat gpt sid that assert in is used to make sure that
        #somehting is in a list or dictionary so that is why I picked that