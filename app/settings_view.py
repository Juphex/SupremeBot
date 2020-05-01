from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
#from jnius import autoclass, cast

#activity = autoclass("org.kivy.android.PythonActivity").mActivity
#Context = autoclass("android.content.Context")

class SettingsView(BoxLayout):
    def __init__(self, orientation="vertical", **kwargs):
        super(SettingsView, self).__init__(**kwargs)
        self.btn = Button(text="SETTINGS //TODO")
        self.btn.bind(on_press = self.switch_screen)
        self.add_widget(self.btn)

    def switch_screen(self, instance):
        self.manager.current = "view"
