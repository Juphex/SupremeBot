import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from View_Screen import ViewScreen
from Settings_Screen import SettingsScreen
from Login_Screen import LoginScreen

class SupremeBot(App):
    def build(self):
        return sm
        
if __name__ == "__main__":
    sm = ScreenManager()

    sm.add_widget(LoginScreen(name="login"))
    sm.add_widget(ViewScreen(name='view'))
    sm.add_widget(SettingsScreen(name='settings'))

    SupremeBot().run()