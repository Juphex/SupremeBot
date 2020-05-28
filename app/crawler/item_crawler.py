from .get_items import Get_Items
from .get_info import Get_Info
from .categories import Categories

class Item_Crawler():
    def __init__(self):
        self.categories = Categories
        self.get_items = Get_Items()
        self.get_info = Get_Info()
       # self.items_all = self.get_info.get(self.items_all)
        self.items = {}

 #   def refresh(self, category):
   #     self.items_all = self.get_items.get_items("https://www.supremenewyork.com/shop/all/shirts")
   #     self.items_all = self.get_info.get(self.items_all)
    
    def getItemsInfo(self, category):
        if "new" not in self.items.keys():
            raise ValueError ("category does not exist in dict1")

        if category not in self.categories.categories.keys():
            raise ValueError("category does not exist in dict")
        #get data
        self.items[category] = self.get_info.get(self.items[category])
        #return data
        return self.items[category]

    def getSpecificItemInfo(self, item):
        return self.get_info.get(item)

    def getItems(self, category):
        if category not in self.categories.categories.keys():
            raise "category does not exist in dict"
        #get data
        self.items[category] = self.get_items.get_items(self.categories.get_url_from_category(category))
        #return data
        return self.items[category]

    def getSoldOutStatus(self, item):
        return self.get_info.get_sold_out_status(item)

    def getNew(self):
        return self.getItems("new")
    
    def infoNew(self):        
        return self.getItemsInfo("new")

    def getJackets(self):
        return self.getItems("jackets")
    
    def infoJackets(self):        
        return self.getItemsInfo("jackets")

    def getShirts(self):
        return self.getItems("shirts")
    
    def infoShirts(self):
        return self.getItemsInfo("shirts")

    #tops_sweaters
    def getTops(self):
        return self.getItems("tops_sweaters")

    def infoTops(self):
        return self.getItemsInfo("tops_sweaters")
    
    def getSweatshirts(self):
        return self.getItems("sweatshirts")

    def infoSweatshirts(self):
        return self.getItemsInfo("sweatshirts")

    def getPants(self):
        return self.getItems("pants")

    def infoPants(self):
        return self.getItemsInfo("pants")

    def getHats(self):
        return self.getItems("hats")
    
    def infoHats(self):
        return self.getItemsInfo("hats")

    def getBags(self):
        return self.getItems("bags")

    def infoBags(self):
        return self.getItemsInfo("bags")

    def getAccessories(self):
        return self.getItems("accessories")
    
    def infoAccessories(self):
        return self.getItemsInfo("accessories")

    def getShoes(self):
        return self.getItems("shoes")

    def infoShoes(self):
        return self.getItemsInfo("shoes")

    def getSkate(self):
        return self.getItems("skate")

    def infoSkate(self):
        return self.getItemsInfo("skate")