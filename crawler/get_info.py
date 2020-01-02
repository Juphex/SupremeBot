from crawler import Crawler

#adds further infos to given items
#status=None, sizes=None, price=None
class Get_Info(Crawler):
    def __init__(self):
        super(Get_Info, self).__init__()

    #Items can be one item or list
    def get(self, items):
        #determine wether items is list
        if len(items) > 1:
            for item in items:
                #check of sold out
                url = item.link
                request = self.rq.get(url)
                response = self.TextResponse(url, body=request.content)
                item.name = response.css("div > h1[itemprop='name']::text").get()
                item.model = response.css("div > p[itemprop='model']::text").get()
                item.price = response.css("div > p[itemprop='price']::text").get()
                item.sizes = response.css("select[id='size'] > option").get()
        else:
                url = items.link
                request = self.rq.get(url)
                response = self.TextResponse(url, body=request.content)
                items.name = response.css("div > h1[itemprop='name']::text").get()
                items.model = response.css("div > p[itemprop='model']::text").get()
                items.price = response.css("div > p[itemprop='price']::text").get()
                items.sizes = response.css("select[id='size'] > option").get()

        return items

    #TESTMETHOD
    def get_url(self,url):
        request = self.rq.get(url)
        response = self.TextResponse(url, body=request.content)
        print(response.css("div > h1[itemprop='name']::text").get())
        print(response.css("div > p[itemprop='model']::text").get())
        print(response.css("p > span[itemprop='price']::text").get())
        print(response.css("select[id='size'] > option").get())
        