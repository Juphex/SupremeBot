import requests as rq
from scrapy.http import TextResponse

#enable to load https for e.g. AsyncImage
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class Crawler:
    def __init__(self):
        self.rq = rq
        self.TextResponse = TextResponse