import requests as rq
from scrapy.http import TextResponse

class Crawler():
    def __init__(self, url):
        self.url = url
        self.rq = rq
        self.TextResponse = TextResponse

    def get_response(self):
        request = self.rq.get(self.url)
        response = self.TextResponse(self.url, body=request.content)
        return response
