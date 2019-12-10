from .crawler import Crawler

class Get_Items(Crawler):
    def get_items(self):
        request = self.rq.get(self.url)
        response = self.TextResponse(self.url, body=request.content)
        baseurl = "https://www.supremenewyork.com/"

        items = []
        #save in order: [name, link, image, sold_out status]
        for article in response.css("div.inner-article"):
            link = baseurl + str(article.css("a::attr(href)").get())
            image = article.css("a > img::attr(src)").get()[2:]
            sold_out = article.css("a > div::text").get()
            name = article.css("h1 > a::text").get()
            items.append([name, link, image, sold_out])

        return items