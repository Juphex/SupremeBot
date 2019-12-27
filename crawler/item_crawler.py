from get_items import Get_Items
from get_info import Get_Info

class Item_Crawler():
    def __init__(self, url):
        self.get_items = Get_Items("https://www.supremenewyork.com/")
        self.items_all = self.get_items.get_items("https://www.supremenewyork.com/shop/all")
