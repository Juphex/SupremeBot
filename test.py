#!/usr/bin/env python

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

## Un-comment if you wish to add to the action view via Python
# from kivy.uix.actionbar import ActionButton, ActionGroup

kv = """
#:import Window kivy.core.window.Window

<SomeLayout_GridLayout>:
    cols: 1
    rows: 2
    row_force_default: True
    rows_minimum: {0: ActionBar.height, 1: self.height - ActionBar.height}
    SomeMenu_ActionBar:
        id: ActionBar

<SomeMenu_ActionBar@ActionBar>:
    ActionView:
        id: ActionView
        ## Choose one of the following
        # HiddenIcon_ActionPrevious: ## Hide just the icon, but keep the text
        # HiddenText_ActionPrevious: ## Keep the icon and UI methods but hide the text
        # Hidden_ActionPrevious: ## Hide both and other widgets go to the right
        Hide_ActionPrevious: ## Hide both and other widgets go to the left

        ## Do the ActionGroup(s) with ActionButton(s) within thing
        ActionGroup:
            id: App_ActionGroup
            mode: 'spinner'
            text: 'App'
            ActionButton:
                text: 'Settings'
                on_press: app.open_settings()
            ActionButton:
                text: 'Quit'
                on_press: app.get_running_app().stop()

        ActionGroup:
            id: File_ActionGroup
            mode: 'spinner'
            text: 'File'
            ActionButton:
                text: 'Open'
            ActionButton:
                text: 'Save'

## Inspired by: https://stackoverflow.com/a/36201399/2632107
## Hide just the icon, but keep the text, note though
##  that one will lose the 'on_press' and similar methods
<HiddenIcon_ActionPrevious@ActionPrevious>:
    title: app.title if app.title is not None else 'Action Previous'
    with_previous: False
    app_icon: ''
    app_icon_width: 0
    app_icon_height: 0
    size_hint_x: None
    width: len(self.title) * 10

## Keep the icon and UI methods but hide the text
<HiddenText_ActionPrevious@ActionPrevious>:
    with_previous: False
    on_press: print(self)
    title: ''

## Hide both but keep ActionGroup(s) and or ActionButton(s) to the right
<Hide_ActionPrevious@ActionPrevious>:
    with_previous: False
    on_press: print(self)
    title: ''
    app_icon: ''
    app_icon_width: 0
    app_icon_height: 0

## Hide everything and allow ActionGroup(s) and or ActionButton(s) to pull to the left
<Hidden_ActionPrevious@ActionPrevious>:
    with_previous: False
    on_press: print(self) ## method that will not be called easily
    title: '' ## Try placing text here, only a few pixels should show
    size_hint: None, None
    size: 0, 0
"""


class SomeLayout_GridLayout(GridLayout):
    pass


class SomeApp(App):
    def build(self):
        ## Cannot set this in '__init__' for some reason
        self.title = 'Some Sweet App'

        Builder.load_string(kv)

        some_layout = SomeLayout_GridLayout()
        ## Uncomment next line if ya wish to use 'add_widget'
        ##  method on ActionView and add ActionGroup(s) and/or
        ##  ActionButton(s) via Python
        # some_actionview = some_layout.ids.ActionBar.ids.ActionView
        return some_layout

if __name__ == '__main__':
    SomeApp().run()
