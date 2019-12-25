import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from login import Login
from dashboard import Dashboard

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        login_page = Login()
        self.add_widget(login_page)

class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super(DashboardScreen, self).__init__(**kwargs)
        dashboard = Dashboard("sd")
        #self.add_widget(dashboard)



class SupremeBot(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(LoginScreen(name="Login"))
        screen_manager.add_widget(DashboardScreen(name="Dashboard"))
        screen_manager.current = "Login"

        return screen_manager
        
if __name__ == "__main__":
    SupremeBot().run()