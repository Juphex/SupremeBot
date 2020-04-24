from .crawler import Crawler

#adds further infos to given items
#status=None, sizes=None, price=None
class Get_Info(Crawler):
    def __init__(self):
        super(Get_Info, self).__init__()

    def __get_info(self, item):
        url = item.link
        request = self.rq.get(url)
        response = self.TextResponse(url, body=request.content)
        #TODO check of sold out
        name = response.css("div > h1[itemprop='name']::text").get()
        model = response.css("div > p[itemprop='model']::text").get()
        price = response.css("div > p[itemprop='price']::text").get()
        sizes = response.css("select[id='size'] > option").get()

        return name, model, price, sizes

    #Items can be one item or list
    def get(self, items):
        #determine wether items is list
        if len(items) >= 1:
            for item in items:
                name, model, price, sizes = self.__get_info(item)
                item.name = name
                item.model = model
                item.price = price
                item.sizes = sizes

        return items
    
    def get_specificItem(self, item):
        #check of sold out
        name, model, price, sizes = self.__get_info(item)
        item.name = name
        item.model = model
        item.price = price
        item.sizes = sizes
        return item

    #TESTMETHOD
    def get_url(self,url):
        request = self.rq.get(url)
        response = self.TextResponse(url, body=request.content)
        print(response.css("div > h1[itemprop='name']::text").get())
        print(response.css("div > p[itemprop='model']::text").get())
        print(response.css("p > span[itemprop='price']::text").get())
        print(response.css("select[id='size'] > option").get())
