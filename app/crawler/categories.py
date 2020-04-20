class Categories:
    #static dict
    categories = {"all" : "https://www.supremenewyork.com/shop/all",
        "new" : "https://www.supremenewyork.com/shop/new",
        "jackets" : "https://www.supremenewyork.com/shop/all/jackets",
        "shirts" : "https://www.supremenewyork.com/shop/all/shirts",
        "tops_sweaters" : "https://www.supremenewyork.com/shop/all/tops_sweaters",
        "sweatshirts" : "https://www.supremenewyork.com/shop/all/sweatshirts",
        "pants" : "https://www.supremenewyork.com/shop/all/pants",
        "hats" : "https://www.supremenewyork.com/shop/all/hats",
        "bags" : "https://www.supremenewyork.com/shop/all/bags",
        "accessories" : "https://www.supremenewyork.com/shop/all/accessories",
        "shoes" : "https://www.supremenewyork.com/shop/all/shoes",
        "skate" : "https://www.supremenewyork.com/shop/all/skate"}
    
    #was static before
    def get_url_from_category(self, category):
        #TODO exception
        return Categories.categories[category]