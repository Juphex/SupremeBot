from dashboard import Dashboard

from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.bubble import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.username = ""
        self.password = ""

        self.layout = GridLayout()
        self.layout.cols = 1
        self.layout.rows = 3

        self.inner_layout = GridLayout(row_force_default=True, row_default_height=60,
                padding= [100,100,100,100])

        kwargs = {"size_hint_x": None,
                "width": 100}

        self.inner_layout.cols = 2
        self.inner_layout.add_widget(Label(text="Username:"))
        self.username_input = TextInput(multiline=False,)
        self.inner_layout.add_widget(self.username_input)

        self.inner_layout.add_widget(Label(text="Password:"))
        self.password_input = TextInput(multiline=False,password=True)
        self.inner_layout.add_widget(self.password_input)

        #TODO
        self.inner_layout.add_widget(Label(text="Save credentials:"))
        self.save_credentials = CheckBox()
        self.inner_layout.add_widget(self.save_credentials)

        self.button_layout = GridLayout(padding=[200,50,200,200])
        self.button_layout.cols = 1
        self.submit_button = Button(text="Submit")
        self.button_layout.add_widget(self.submit_button)
        self.submit_button.bind(on_press=self.verifyLogin)

        self.layout.add_widget(self.inner_layout)
        self.layout.add_widget(self.button_layout)
        self.add_widget(self.layout)

    def verifyLogin(self, instance):
        self.username = self.username_input.text
        self.password = self.password_input.text

        #Verify with Database
        success = True
        if success == True:
            self.manager.current = "view"
        elif success == False:
            #button in popup
            content = Button(text='Try again', padding=(100,100))
            popup = Popup(title='Login failed', content=content,
                size_hint=(0.4,0.5))

            content.bind(on_press=popup.dismiss)
            popup.open()
