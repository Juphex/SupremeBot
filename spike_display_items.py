from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.actionbar import ActionPrevious, ActionButton, ActionBar, ActionGroup, ActionView, ActionItem
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from crawler.get_items import Get_Items
from crawler.get_names import Get_Names
from kivy.uix.image import AsyncImage
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from enum import Enum

class Sizes(Enum):
    SMALL = 0
    MEDIUM = 1
    LARGE = 2
    XLARGE = 3

#REFRESH BUTTON
#REFRESH ON DROP
#BACKGROUND SERVICE?

class Order:
    def buy(link):
        #get info
        #send
        print("Buying")

class Item(BoxLayout):
    #image is either downloaded or link? //Async Image
    def __init__(self, name, link, image_src, status, size=Sizes.MEDIUM, **kwargs):
        super(Item, self).__init__(**kwargs)
        self.img = AsyncImage(source=image_src, size_hint=(1,1))
        #self.img.width = 200
        #self.img.height = 200
        self.name = name
        self.link = link
        self.status = status
        self.add_widget(self.img)
        self.buy_btn = Button(text="Buy now", size_hint=(1,0.1))
        self.buy_btn.bind(on_press=self.buy_item)
        self.info_layout = GridLayout()
        self.info_layout.cols = 1
        self.info_layout.rows = 4

        self.sizes = DropDown()
        for i in range(len(Sizes)):
            btn = Button(text=Sizes(i).name, size_hint_y=None)
            btn.bind(on_release=lambda btn: self.sizes.select(btn.text))
            self.sizes.add_widget(btn)
        self.mainbutton = Button(text=size.name, size_hint=(1, 0.1))
        self.mainbutton.bind(on_release=self.sizes.open)
        self.sizes.bind(on_select=lambda instance, x: setattr(self.mainbutton, "text", x))

        self.info_layout.add_widget(Label(text=str(self.status), size_hint=(1,0.1)))
        self.info_layout.add_widget(self.mainbutton)
        self.info_layout.add_widget(self.buy_btn)
        self.add_widget(self.info_layout)

    def buy_item(self, instance):
        return Order.buy(self.link)
    #def buy() #read data from db
            

class Items(GridLayout):
    def __init__(self, **kwargs):
        super(Items, self).__init__(**kwargs)
        self.crawler = Get_Items("https://www.supremenewyork.com/shop/all/")
        #save in order: [name, link, image, sold_out status]
        self.items = self.crawler.get_items()
        self.display_items()
        #self.rows=4
        self.cols=3
        self.spacing = 10
        for i in range(len(self.items)):
            item = self.items[i]
            src = "http://" + str(item[2])
            self.add_widget(Item(item[0], item[1], src, item[3], size_hint_y=None))
    
    def refresh(self):
        self.items = self.crawler.get_items()
        self.display_items()
    
    def display_items(self):
        print("hi")

class DashBoard(BoxLayout):
    def __init__(self, **kwargs):
        super(DashBoard, self).__init__(**kwargs)
        self.orientation = "horizontal"
        self.add_widget(Button(size_hint=(0.2,1)))
        #self.add_widget(Label(text="Hallo"))
        self.items = Items(size_hint_y=None)
        self.items.bind(minimum_height=self.items.setter('height'))

        self.scroll = ScrollView(size_hint=(1,None),size=(Window.width, Window.height))
        self.scroll.add_widget(self.items)
        self.add_widget(self.scroll)

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
# Declare both screens
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.add_widget(DashBoard())

    def switch_screen(self, instance):
       print("")
       self.manager.current = "settings"

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.btn = Button(text="Menu Screen")
        self.btn.bind(on_press = self.switch_screen)
        self.add_widget(self.btn)
    def switch_screen(self, instance):
        self.manager.current = "menu"

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()
