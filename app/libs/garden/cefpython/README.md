CEF browser widget
==================

This is a widget that embeds [cefpython](https://code.google.com/p/cefpython)
into a Kivy widget.

It has been tested only on Linux 64bit so far.

This fork only works for python3 and above. For python2 application please 
make your own changes to accomodate to your use.


Example
-------

    from kivy.app import App
    from kivy.garden.cefpython import CEFBrowser

    class SimpleBrowserApp(App):
        def build(self):
            return CEFBrowser(url="http://kivy.org")
    SimpleBrowserApp().run()


Status
------

This project shouldn't be considered stable. There are many things, as 
e.g. downloads which aren't implemented or causing proplems.
Tested on Ubuntu 14.04.1 LTS 64bit with the following debian packages
installed:
- `libnss3-1d`
- `libnspr4-0d`

If it does not work on Windows, it is most probably because not all the
needed DLLs are copied correctly from the downloaded ZIP file. You would then
need to edit `lib/cefpython_sources.json`.


How to develop with garden.cefpython
-------------------------------------------------------

1. Install kivy into virtualenv (consult kivy docs for this)
2. Install required dependencies `pip install -r requirements.txt`
3. Symlink cefbrowser into graden directory: `ln -s path/to/garden.cefpython ~/.kivy/garden/garden.cefpython`
4. Now you should be able to launch one of the examples: `python examples/minimal.py`



Known Issues
------------

- Documentation is poor
- API (Methods of CEFBrowser) *will* still be subject to change
- Keyboards sometimes don't vanish, when another element is focused, system
    keyboard input is sometimes redirected to multiple focused elements, etc.


Contribute
----------

- Test on all operating systems and file bug reports
