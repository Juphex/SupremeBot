from get_items import Get_Items
from get_info import Get_Info

class Item_Crawler():
    def __init__(self, url):
        self.get_items = Get_Items("https://www.supremenewyork.com/")
        self.items_all = self.get_items.get_items("https://www.supremenewyork.com/shop/all")
        #ADD CATEGORIES
        self.get_info = Get_Info()
        self.items_all = self.get_info.get(self.items_all)

    def refresh(category):
        self.items_all = self.get_items.get_items("https://www.supremenewyork.com/shop/all")
        self.items_all = self.get_info.get(items_all)