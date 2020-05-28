from kivy.uix.gridlayout import GridLayout
from item import DisplayItem


class DisplayItemsLayout(GridLayout):
    def __init__(self, items, driver, **kwargs):
        super(DisplayItemsLayout, self).__init__(**kwargs)
        self.cols = 2
        #horizontal, vertical
        self.spacing = [0, 10]
        self.padding = [-50,53,0,0]
        self.displayItems = []
        for item in items:
            new_item = DisplayItem(item, driver, size_hint_y=None, orientation="horizontal")
            self.add_widget(new_item)
            self.displayItems.append(new_item)

    def updateDriver(self, driver):
        for item in self.displayItems:
            item.set_driver(driver)

    # update non sold_outs info
    def refreshStatus(self, crawler):
        for item in self.displayItems:
            if item.status is not "sold out":
                sold_out_bool = crawler.getSoldOutStatus(item)
                item.set_status_sold_out(sold_out_bool)