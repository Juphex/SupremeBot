import requests as rq
from scrapy.http import TextResponse

class Crawler:
    def __init__(self):
        self.rq = rq
        self.TextResponse = TextResponse