#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Minimal example of the CEFBrowser widget use. Here you don't have any controls
(back / forth / reload) or whatsoever. Just a kivy app displaying the
chromium-webview.
"""


from kivy.app import App
from cefbrowser import CEFBrowser


if __name__ == '__main__':
    class SimpleBrowserApp(App):
        def build(self):
            cb =  CEFBrowser(url="http://google.de")
            return cb

    SimpleBrowserApp().run()
