from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.bubble import Button


class Dashboard(GridLayout):
    def __init__(self, username, **kwargs):
        super(Dashboard, self).__init__(**kwargs)
        print("DASHBOARD")
        self.layout = BoxLayout(padding=10)
        self.button = Button(text='My first button')
        self.layout.add_widget(self.button)
