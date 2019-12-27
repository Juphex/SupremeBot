from crawler import Crawler

#adds further infos to given items
#status=None, sizes=None, price=None
class Get_Info(Crawler):
    def get(self, items):
        for item in items:
            if item[0] == None:
                request = self.rq.get(item[1])
                response = self.TextResponse(item[1], body=request.content)
                item[0] = response.css("p[itemprop=description]::text").get()
        return items

