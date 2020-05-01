import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from view_screen import ViewScreen
from login_screen import LoginScreen
from kivy.app import runTouchApp

from crawler.item_crawler import Item_Crawler


class SupremeBot(App):
    def build(self):
        return sm
        
if __name__ == "__main__":
    item_crawler = Item_Crawler()

    sm = ScreenManager()
    sm.add_widget(LoginScreen(name="login"))
    sm.add_widget(ViewScreen(item_crawler, name='view'))
    SupremeBot().run()
