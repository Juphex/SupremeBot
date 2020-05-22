import kivy
from kivy.app import App
from kivy.app import runTouchApp
from kivy.uix.screenmanager import ScreenManager
from view_screen import ViewScreen
from login_screen import LoginScreen
from kivy.uix.settings import SettingsWithNoMenu


from crawler.item_crawler import Item_Crawler
from settings.settingsjson import settings_json


class SupremeBot(App):
    def build(self):
        self.settings_cls = SettingsWithNoMenu
        self.use_kivy_settings = False
        return sm

    def build_config(self, config):
        config.setdefaults('credentials', {
            'size': "medium",
            'name': "Firstname Lastname",
            'email': '',
            'tel': '00000',
            "street" : "",
            "street_nr":"",
            "address_3":"",
            "city":"",
            "plz":"",
            "country":"UK"})

    def build_settings(self, settings):
        settings.add_json_panel('Settings',
                                self.config,
                                data=settings_json)

    def on_config_change(self, config, section,
                         key, value):
        print (config, section, key, value)

if __name__ == "__main__":
    item_crawler = Item_Crawler()

    sm = ScreenManager()
    sm.add_widget(LoginScreen(name="login"))
    sm.add_widget(ViewScreen(item_crawler, name='view'))
    SupremeBot().run()
