from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label

class DisplayItem(BoxLayout):
    def __init__(self, item, **kwargs):
        super(DisplayItem, self).__init__(**kwargs)
        self.item = item
        self.img = AsyncImage(source=self.item.img_src, size_hint=(1,1))
        self.img.width = 200
        self.img.height = 200
        self.name = self.item.name
        self.link = self.item.link
        self.status = self.item.status

        self.add_widget(self.img)
        self.buy_btn = Button(text="Buy", size_hint=(1,0.1))
        self.buy_btn.bind(on_press=self.buy_item)
        self.info_layout = GridLayout()
        self.info_layout.cols = 1
        self.info_layout.rows = 4

        #Case item has no options
        if self.item.sizes is not None:
            self.sizes = DropDown()
            for size in self.item.sizes:
                btn = Button(text=size, size_hint_y=None)
                btn.bind(on_release=lambda btn: self.sizes.select(btn.text))
                self.sizes.add_widget(btn)

            #set default value to item.sizes
            self.mainbutton = Button(text=self.item.sizes[0], size_hint=(1, 0.1))
            self.mainbutton.bind(on_release=self.sizes.open)
            self.sizes.bind(on_select=lambda instance, x: setattr(self.mainbutton, "text", x))
            self.info_layout.add_widget(self.mainbutton)

        self.info_label = Label(text=str(self.status), size_hint=(1,0.1), markup=True)
        self.info_layout.add_widget(self.info_label)
        if self.status is None:
            self.info_label.text = "[color=00ff00]In Stock[/color]"
            self.info_layout.add_widget(self.buy_btn)
        else:
            self.info_label.text = "[color=ff0000][b][size=15]OUT OF STOCK[/size][/b][/color]"

        self.add_widget(self.info_layout)

    def buy_item(self, instance):
        #return Order.buy(self.link)
        #HERE:
        #Order.buy... 
        print("Buy Logic to implement")
