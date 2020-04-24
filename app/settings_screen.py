from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
#from jnius import autoclass, cast

#activity = autoclass("org.kivy.android.PythonActivity").mActivity
#Context = autoclass("android.content.Context")

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.btn = Button(text="SETTINGS //TODO")
        self.btn.bind(on_press = self.switch_screen)
        self.add_widget(self.btn)

    def switch_screen(self, instance):
        self.manager.current = "view"
