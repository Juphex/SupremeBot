from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.actionbar import ActionPrevious, ActionButton, ActionBar, ActionGroup, ActionView, ActionItem
from navigationbar import NavigationBar
from item import DisplayItem


class ViewScreen(Screen):
    def __init__(self, item_crawler, **kwargs):
        super(ViewScreen, self).__init__(**kwargs)
        #navbar
        self.navbar = NavigationBar()
        #self.navbar.button_home.bind(on_press=self.show_navbar)
        self.navbar.button_category.bind(on_press=self.selenium)
        self.navbar.button_settings.bind(on_press=lambda x:self.switch_screen("settings"))
        self.add_widget(self.navbar)

        #action bar
        #add refresh button?
        #status of items
        self.actnbr = ActionBar(pos_hint = {"top" : 1})
        self.actnvw = ActionView(use_separator=True)
        self.group = ActionGroup(text = "Supreme App1")
        self.actnvw.add_widget(self.group)

        #app_icon in ActionPrevious
        self.actnprv = ActionPrevious(inside_group=True, title="Supreme App", with_previous=False, on_press=self.show_navbar)
        self.actnvw.add_widget(self.actnprv)
        self.actnbr.add_widget(self.actnvw)
        self.add_widget(self.actnbr)

        self.items = item_crawler.items_all
        for item in self.items:
            self.add_widget(DisplayItem(item, size_hint_y=None))


    def show_navbar(self, instance):
        self.navbar.toggle_state()

    def switch_screen(self, screen):
       self.manager.current = screen

    #random func
    def selenium(self, instance):
        self.navbar.button_category.text = "hihihi"
        print("hi")