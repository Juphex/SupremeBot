class Item():
    def __init__(self, name, link, img_src, status=None, sizes=None, price=None, category=None,\
        model=None):
        self.name = name
        self.link = link
        self.img_src = img_src
        self.status = status
        self.sizes = sizes
        self.price = price
        self.category = category
        self.model = model
    
    def sold_out(self):
        #check if working
        if sold_out == "sold out":
            return True

        return False
    
    #Override
    def __len__(self):
        return 1