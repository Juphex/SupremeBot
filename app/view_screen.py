from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.actionbar import ActionPrevious, ActionButton, ActionBar, ActionGroup, ActionView, ActionItem
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from navigationbar import NavigationBar
from displaylayout import DisplayItemsLayout
from item import DisplayItem


class ViewScreen(Screen):
    def __init__(self, item_crawler, **kwargs):
        super(ViewScreen, self).__init__(**kwargs)
        #action bar
        #add refresh button?
        #status of items
        self.actnbr = ActionBar(pos_hint = {"top" : 1})
        self.actnvw = ActionView(use_separator=True)
        self.group = ActionGroup(text = "Supreme App")
        #self.actnvw.add_widget(self.group, 1)

        #navbar
        self.navbar = NavigationBar()
        self.navbar.button_home.bind(on_press=self.show_navbar)
        self.navbar.button_category.bind(on_press=self.selenium)
        self.navbar.button_settings.bind(on_press=lambda x:self.switch_screen("settings"))

        #app_icon in ActionPrevious
        self.actnprv = ActionPrevious(inside_group=True, title="Supreme App             [b]New Items[/b]", with_previous=False, on_press=self.show_navbar, markup=True)
        self.actnvw.add_widget(self.actnprv)
        self.actnbr.add_widget(self.actnvw)

        #Scollview
        self.items = item_crawler.getNew()
        self.items_layout = DisplayItemsLayout(self.items, size_hint_y=None)
        self.items_layout.bind(minimum_height=self.items_layout.setter('height'))
        self.screenview = ScrollView(size_hint=(1, 1))
        self.screenview.add_widget(self.items_layout)

        #NAVBAR currently disabled
        '''
        self.inside_baselayout = BoxLayout(orientation="horizontal")
        self.inside_baselayout = FloatLayout(size=(Window.width, Window.height - 10 * Window.height))
        self.inside_baselayout.add_widget(self.sv ,-1)
        self.inside_baselayout.add_widget(self.navbar, 1)
        self.baselayout.add_widget(self.inside_baselayout)'''
        self.baselayout = BoxLayout(orientation="vertical")
        self.baselayout.add_widget(self.actnbr)
        self.baselayout.add_widget(self.screenview, -1)
        self.add_widget(self.baselayout)

        
    def show_navbar(self, instance):
        self.navbar.toggle_state()

    def switch_screen(self, screen):
       self.manager.current = screen

    #random func
    def selenium(self, instance):
        self.navbar.button_category.text = "hihihi"
        print("hi")