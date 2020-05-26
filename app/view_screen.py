from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.actionbar import ActionPrevious, ActionButton, ActionBar, ActionGroup, ActionView, ActionItem
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.scrollview import ScrollView
#from navigationbar import NavigationBar
from displaylayout import DisplayItemsLayout

class ViewScreen(Screen):
    def __init__(self, item_crawler, **kwargs):
        super(ViewScreen, self).__init__(**kwargs)
        #action bar
        #add refresh button?
        #status of items
        self.actnbr = ActionBar(pos_hint = {"top" : 1})
        self.actnvw = ActionView(use_separator=True)
        self.group = ActionGroup(text = "Supreme App")
        #self.actnvw.add_widget(self.group, 1)


        #app_icon in ActionPrevious
        self.actnprv = ActionPrevious(inside_group=True, title="Supreme App             [b]New Items[/b]", with_previous=False, on_press=self.return_to_dashboard, markup=True)
        self.actnvw.add_widget(self.actnprv)
        self.settings_button = ActionButton(text="Settings")
        self.settings_button.bind(on_press=self.switch_screen_to_settings)
        self.actnvw.add_widget(self.settings_button)
        self.actnbr.add_widget(self.actnvw)

        #Scollview
        self.items = item_crawler.getNew()
        self.items_layout = DisplayItemsLayout(self.items, size_hint_y=None)
        self.items_layout.bind(minimum_height=self.items_layout.setter('height'))
        self.screenview = ScrollView(size_hint=(1, 1))
        self.screenview.add_widget(self.items_layout)

        self.baselayout = BoxLayout(orientation="vertical")
        self.baselayout.add_widget(self.actnbr)
        self.baselayout.add_widget(self.screenview, -1)
        self.add_widget(self.baselayout)


        self.settings_is_active = False
        self.dashboard_is_active = True

    #may be obsolete
    def return_to_dashboard(self, instance):
        if self.settings_is_active:
            self.baselayout.remove_widget(self.settingsview)
            # TODO: refresh screenview
            self.baselayout.add_widget(self.screenview)

            self.settings_is_active = False
            self.dashboard_is_active = True

    def switch_screen_to_settings(self, instance):
        App.get_running_app().open_settings()