from .crawler import Crawler

class Get_Names(Crawler):
    #first position of list is name
    def get_names_from_items(items):
        for item in items:
            if item[0] == None:
                request = self.rq.get(item[1])
                response = self.TextResponse(item[1], body=request.content)
                item[0] = response.css("p[itemprop=description]::text").get()
        return items