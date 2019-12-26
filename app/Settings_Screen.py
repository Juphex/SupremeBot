from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.btn = Button(text="Menu Screen")
        self.btn.bind(on_press = self.switch_screen)
        self.add_widget(self.btn)
    def switch_screen(self, instance):
        self.manager.current = "view"
