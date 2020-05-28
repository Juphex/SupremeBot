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
        name, model, price, sizes = self.__get_info(item)
        item.name = name
        item.model = model
        item.price = price
        item.sizes = sizes
        return item

    def get_sold_out_status(self, item):
        sold_out_status = False
        url = item.link
        request = self.rq.get(url)
        response = self.TextResponse(url, body=request.content)
        sold_out_btn_content = response.css("#add-remove-buttons > b").get()
        if sold_out_btn_content == "<b class=\"button sold-out\">sold out</b>":
            sold_out_status = True

        return sold_out_status