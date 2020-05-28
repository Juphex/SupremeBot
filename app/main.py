from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from view_screen import ViewScreen
from login_screen import LoginScreen
from kivy.uix.settings import SettingsWithNoMenu
from kivy.config import ConfigParser


from crawler.item_crawler import Item_Crawler
from settings.settingsjson import settings_json


class SupremeBot(App):
    def build(self):
        self.settings_cls = SettingsWithNoMenu
        self.use_kivy_settings = False
        return sm

    def build_config(self, config):
        config.setdefaults('credentials', {
            'size': "Medium",
            'name': "Firstname Lastname",
            'email': '',
            'tel': '00000',
            "street" : "",
            "street_nr":"",
            "address_3":"",
            "city":"",
            "plz":"",
            "country":"UK"})
        config.setdefaults("payment", {
            "credit_card_type" : "Visa",
            "credit_card_nr":"",
            "credit_card_exp_month":"01",
            "credit_card_exp_year":"2020",
            "credit_card_cvv":""
        })

    def get_size(self):
        config = ConfigParser()
        config.read('supremebot.ini')
        size = config.get("credentials", "size")
        return str(size)

    def get_adress_details(self):
        config = ConfigParser()
        config.read('supremebot.ini')
        name = config.get("credentials", "name")
        email = config.get("credentials", "email")
        tel = config.get("credentials", "tel")
        street = config.get("credentials", "street")
        street_nr = config.get("credentials", "street_nr")
        address_3 = config.get("credentials", "address_3")
        city = config.get("credentials", "city")
        #postal code
        plz = config.get("credentials", "plz")
        country = config.get("credentials", "country")

        return name, email, tel, street, street_nr, address_3, city, plz, country

    def get_payment_deatils(self):
        config = ConfigParser()
        config.read('supremebot.ini')
        credit_card_type = config.get("payment", "credit_card_type")
        credit_card_nr = config.get("payment", "credit_card_nr")
        credit_card_exp_month = config.get("payment", "credit_card_exp_month")
        credit_card_exp_year = config.get("payment", "credit_card_exp_year")
        credit_card_exp_cvv = config.get("payment", "credit_card_cvv")

        return credit_card_type, credit_card_nr, credit_card_exp_month, credit_card_exp_year, credit_card_exp_cvv

    def build_settings(self, settings):
        settings.add_json_panel('Settings (Press ESC to close)',
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