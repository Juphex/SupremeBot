from cefpython3 import cefpython as cef
from libs.garden.cefpython.cefbrowser import CEFBrowser
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout

class Scrceen(Screen):
    def __init__(self, **kwargs):
        super(Scrceen, self).__init__(**kwargs)
        cef.Initialize()
        browser =  cef.CreateBrowserSync(url="https://www.google.de", window_title="Hello World!")
        #self.add_widget(BoxLayout().add_widget(browser))
        browser.ExecuteJavascript("alert(1);")
        cef.MessageLoop()
        cef.Shutdown()

if __name__ == '__main__':
    class SimpleBrowserApp(App):
        def build(self):
            return Scrceen()

    SimpleBrowserApp().run()
