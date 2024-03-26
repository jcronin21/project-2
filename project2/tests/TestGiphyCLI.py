import unittest
from ..GIPHYCLI import GiphyAPI

class TestGiphyCLI(unittest.TestCase):

    def test_trending_command(self):
        class fake:
            def json(self):
                return{"data":[{"title"}]}
            
            #not done
            