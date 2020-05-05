from kivy.uix.settings import SettingsWithTabbedPanel, SettingsWithNoMenu, SettingsWithSidebar, SettingsWithSpinner
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
#from jnius import autoclass, cast

#activity = autoclass("org.kivy.android.PythonActivity").mActivity
#Context = autoclass("android.content.Context")

class SettingsView(BoxLayout):
    def __init__(self, orientation="vertical", **kwargs):
        super(SettingsView, self).__init__(**kwargs)
        self.btn = Button(text="SETTINGS //TODO")
        self.add_widget(self.btn)
