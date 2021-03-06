class Item():
    def __init__(self, name, link, img_src, status=None, sizes=None, price=None, category=None,\
        model=None):
        self.name = name
        self.link = link
        #changed to http due to ssl error
        self.img_src = "http://" + img_src
        self.status = status
        self.sizes = sizes
        self.price = price
        self.category = category
        #e.g. color
        self.model = model
    
    def sold_out(self):
        #check if working
        if self.status == "sold out":
            return True

        return False
    
    #Override
    def __len__(self):
        return 1