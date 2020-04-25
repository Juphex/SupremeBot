from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.actionbar import ActionPrevious, ActionButton, ActionBar, ActionGroup, ActionView, ActionItem
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label


# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
# Declare both screens
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.btn = Button(text="Menu Screen")
        self.btn.bind(on_press = self.switch_screen)
        self.add_widget(self.btn)

        #action bar
        self.actnbr = ActionBar(pos_hint = {"top" : 1})
        #self.drpdwn = DropDown()
        #self.drpdwn.add_widget(Label(text=u'Hello world ' + chr(2764)))
        self.actnvw = ActionView(use_separator=True)
        #self.actitm = ActionItem()
        #self.actitm.add_widget(self.drpdwn)
        self.group = ActionGroup(text = "Supreme App")
        self.group.add_widget(ActionButton(text="hallo"))
        self.actnvw.add_widget(self.group)

        #app_icon in ActionPrevious
        #on_press: print(self)
        self.actnprv = ActionPrevious(inside_group=True,title="ActPrevious", with_previous=False)
        self.actnvw.add_widget(self.actnprv)
        self.actnbr.add_widget(self.actnvw)
        self.add_widget(self.actnbr)

    def switch_screen(self, instance):
       print("")
       self.manager.current = "settings"

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.btn = Button(text="Menu Screen")
        self.btn.bind(on_press = self.switch_screen)
        self.add_widget(self.btn)
    def switch_screen(self, instance):
        self.manager.current = "menu"

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()
