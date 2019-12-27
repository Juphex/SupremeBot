class Item():
    def __init__(self, name, link, img_src, status=None, sizes=None, price=None, category=None):
        self.name = name
        self.link = link
        self.img_src = img_src
        self.status = status
        self.sizes = sizes
        self.price = price
        self.category = category