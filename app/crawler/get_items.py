from .crawler import Crawler
from .item import Item

class Get_Items(Crawler):
    def __init__(self, base_url):
        super(Get_Items, self).__init__()
        self.base_url = base_url

    def get_items(self, url):
        request = self.rq.get(url)
        response = self.TextResponse(url, body=request.content)

        items = []
        #save in order: [name, link, image, sold_out status]
        for article in response.css("div.inner-article"):
            link = self.base_url + str(article.css("a::attr(href)").get())
            image = article.css("a > img::attr(src)").get()[2:]
            sold_out = article.css("a > div::text").get()
            name = article.css("h1 > a::text").get()
            items.append(Item(name, link, image, status=sold_out))

        return items