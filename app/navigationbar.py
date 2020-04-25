from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from libs.garden.navigationdrawer import NavigationDrawer

#https://github.com/kivy-garden/garden.navigationdrawer#
#https://www.reddit.com/r/kivy/comments/2cniis/hidden_sliding_menu/cji22op/
class NavigationBar(NavigationDrawer):
    def __init__(self, anim_type="slide_above_anim", **kwargs):
        super(NavigationBar, self).__init__(**kwargs)
        side_panel = BoxLayout(orientation='vertical')
        #side_panel.add_widget(Label(text='Supreme Bot'))
        self.button_home = Button(text='Start')
        self.button_category = Button(text='Category 1')
        self.button_settings = Button(text="Settings")

        side_panel.add_widget(self.button_home)
        side_panel.add_widget(self.button_category)
        side_panel.add_widget(self.button_settings)
        self.add_widget(side_panel)

        main_panel = BoxLayout(orientation='vertical')
        self.add_widget(main_panel)