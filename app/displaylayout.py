from kivy.uix.gridlayout import GridLayout
from item import DisplayItem


class DisplayItemsLayout(GridLayout):
    def __init__(self, items, **kwargs):
        super(DisplayItemsLayout, self).__init__(**kwargs)
        self.cols = 2
        self.spacing = 5
        for item in items:
            self.add_widget(DisplayItem(item, size_hint_y=None, orientation="horizontal"))