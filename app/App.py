import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from login import Login
from Menu_Screen import MenuScreen
from Settings_Screen import SettingsScreen

class SupremeBot(App):
    def build(self):
        return sm
        
if __name__ == "__main__":
    sm = ScreenManager()
    sm.add_widget(MenuScreen(name='menu'))
    sm.add_widget(SettingsScreen(name='settings'))

    SupremeBot().run()