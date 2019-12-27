import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from view_screen import ViewScreen
from settings_screen import SettingsScreen
from login_screen import LoginScreen

class SupremeBot(App):
    def build(self):
        return sm
        
if __name__ == "__main__":
    sm = ScreenManager()

    sm.add_widget(LoginScreen(name="login"))
    sm.add_widget(ViewScreen(name='view'))
    sm.add_widget(SettingsScreen(name='settings'))

    SupremeBot().run()