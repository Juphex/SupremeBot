# An example of embedding CEF browser in the Kivy framework.
# The browser is embedded using off-screen rendering mode.

# Tested using Kivy 1.7.2 stable on Ubuntu 12.04 64-bit.

# In this example kivy-lang is used to declare the layout which
# contains two buttons (back, forward) and the browser view.

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, GraphicException
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.base import EventLoop
from kivy.properties import BooleanProperty, StringProperty

####CEF IMPORT ####
import ctypes, os, sys
libcef_so = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'libcef.so')
if os.path.exists(libcef_so):
    # Import local module
    ctypes.CDLL(libcef_so, ctypes.RTLD_GLOBAL)
    if 0x02070000 <= sys.hexversion < 0x03000000:
        import cefpython_py27 as cefpython
    else:
        raise Exception("Unsupported python version: %s" % sys.version)
else:
    # Import from package
    from cefpython3 import cefpython



class CefBrowser(Widget):

    # Keyboard mode: "global" or "local".
    # 1. Global mode forwards keys to CEF all the time.
    # 2. Local mode forwards keys to CEF only when an editable
    #    control is focused (input type=text or textarea).
    keyboard_mode = "local"
    is_loading = BooleanProperty(True)
    touches = []
    url = StringProperty('')
    
    '''Represent a browser widget for kivy, which can be used like a normal widget.
    '''
    def __init__(self, start_url='http://www.google.com/', **kwargs):
        super(CefBrowser, self).__init__(**kwargs)
        
        self.start_url = start_url
        
        #Workaround for flexible size:
        #start browser when the height has changed (done by layout)
        #This has to be done like this because I wasn't able to change 
        #the texture size
        #until runtime without core-dump.
        self.bind(size = self.size_changed)
    

    starting = True
    def size_changed(self, *kwargs):
        '''When the height of the cefbrowser widget got changed, create the browser
        '''
        if self.starting:
            if self.height != 100:
                self.start_cef()
                self.starting = False
        else:
            self.texture = Texture.create(
                size=self.size, colorfmt='rgba', bufferfmt='ubyte')
            self.texture.flip_vertical()
            with self.canvas:
                Color(1, 1, 1)
                # This will cause segmentation fault:
                # | self.rect = Rectangle(size=self.size, texture=self.texture)
                # Update only the size:
                self.rect.size = self.size
            self.browser.WasResized()

   
    def _cef_mes(self, *kwargs):
        '''Get called every frame.
        '''
        cefpython.MessageLoopWork()
        
        
    def _update_rect(self, *kwargs):
        '''Get called whenever the texture got updated. 
        => we need to reset the texture for the rectangle
        '''
        self.rect.texture = self.texture
   
            
    def start_cef(self):
        '''Starts CEF. 
        '''
        # create texture & add it to canvas
        self.texture = Texture.create(
                size=self.size, colorfmt='rgba', bufferfmt='ubyte')
        self.texture.flip_vertical()
        with self.canvas:
            Color(1, 1, 1)
            self.rect = Rectangle(size=self.size, texture=self.texture)

        settings = {
                "release_dcheck_enabled": False, # Enable only when debugging.
                # This directories must be set on Linux
                "locales_dir_path": cefpython.GetModuleDirectory()+"/locales",
                "resources_dir_path": cefpython.GetModuleDirectory(),
                "browser_subprocess_path": "%s/%s" % (cefpython.GetModuleDirectory(), "subprocess")}
        
        #start idle
        Clock.schedule_interval(self._cef_mes, 0)
        
        #init CEF
        cefpython.Initialize(settings)
       
        #WindowInfo offscreen flag
        windowInfo = cefpython.WindowInfo()
        windowInfo.SetAsOffscreen(0)
        
        #Create Broswer and naviagte to empty page <= OnPaint won't get called yet
        browserSettings = {}
        # The render handler callbacks are not yet set, thus an 
        # error report will be thrown in the console (when release
        # DCHECKS are enabled), however don't worry, it is harmless.
        # This is happening because calling GetViewRect will return 
        # false. That's why it is initially navigating to "about:blank".
        # Later, a real url will be loaded using the LoadUrl() method 
        # and the GetViewRect will be called again. This time the render
        # handler callbacks will be available, it will work fine from
        # this point.
        # --
        # Do not use "about:blank" as navigateUrl - this will cause
        # the GoBack() and GoForward() methods to not work.
        self.browser = cefpython.CreateBrowserSync(windowInfo, browserSettings, 
                navigateUrl=self.start_url)
        
        #set focus
        self.browser.SendFocusEvent(True)
        
        self._client_handler = ClientHandler(self)
        self.browser.SetClientHandler(self._client_handler)
        self.set_js_bindings()
        
        #Call WasResized() => force cef to call GetViewRect() and OnPaint afterwards
        self.browser.WasResized() 

        # The browserWidget instance is required in OnLoadingStateChange().
        self.browser.SetUserData("browserWidget", self)

        if self.keyboard_mode == "global":
            self.request_keyboard()

        #Clock.schedule_once(self.change_url, 5)
    
    
    _client_handler = None
    _js_bindings = None

    def set_js_bindings(self):
        # When browser.Navigate() is called, some bug appears in CEF
        # that makes CefRenderProcessHandler::OnBrowserDestroyed()
        # is being called. This destroys the javascript bindings in
        # the Render process. We have to make the js bindings again,
        # after the call to Navigate() when OnLoadingStateChange()
        # is called with isLoading=False. Problem reported here:
        # http://www.magpcss.org/ceforum/viewtopic.php?f=6&t=11009

        if not self._js_bindings:
            self._js_bindings = cefpython.JavascriptBindings(
                bindToFrames=True, bindToPopups=True)
            self._js_bindings.SetFunction("__kivy__request_keyboard", 
                    self.request_keyboard)
            self._js_bindings.SetFunction("__kivy__release_keyboard",
                    self.release_keyboard)

        self.browser.SetJavascriptBindings(self._js_bindings)
    

    def change_url(self, url="", *kwargs):
        self.browser.GetMainFrame().ExecuteJavascript(
                "window.location='%s'" %url)
        self._client_handler._reset_js_bindings = True


    _keyboard = None

    def request_keyboard(self):
        print("request_keyboard()")
        wid=Widget(pos=(Window.width/2-100, Window.height/2))
        self._keyboard = EventLoop.window.request_keyboard(
                self.release_keyboard, wid)
        self._keyboard.bind(on_key_down=self.on_key_down)
        self._keyboard.bind(on_key_up=self.on_key_up)
        self.is_shift1 = False
        self.is_shift2 = False
        self.is_ctrl1 = False
        self.is_ctrl2 = False
        self.is_alt1 = False
        self.is_alt2 = False
        # Browser lost its focus after the LoadURL() and the 
        # OnBrowserDestroyed() callback bug. This will only work
        # when keyboard mode is local.
        self.browser.SendFocusEvent(True)


    def release_keyboard(self):
        self.is_shift1 = False
        self.is_shift2 = False
        self.is_ctrl1 = False
        self.is_ctrl2 = False
        self.is_alt1 = False
        self.is_alt2 = False
        if not self._keyboard:
            return
        print("release_keyboard()")
        self._keyboard.unbind(on_key_down=self.on_key_down)
        self._keyboard.unbind(on_key_up=self.on_key_up)
        self._keyboard.release()

    # Kivy does not provide modifiers in on_key_up, but these
    # must be sent to CEF as well.
    is_shift1 = False
    is_shift2 = False
    is_ctrl1 = False
    is_ctrl2 = False
    is_alt1 = False
    is_alt2 = False

    def on_key_down(self, keyboard, keycode, text, modifiers):
        # Notes:
        # - right alt modifier is not sent by Kivy through modifiers param.
        # print("on_key_down(): keycode = %s, text = %s, modifiers = %s" % (
        #         keycode, text, modifiers))
        if keycode[0] == 27:
            # On escape release the keyboard, see the injected
            # javascript in OnLoadStart().
            self.browser.GetFocusedFrame().ExecuteJavascript(
                    "__kivy__on_escape()")
            return
        cefModifiers = cefpython.EVENTFLAG_NONE
        if "shift" in modifiers:
            cefModifiers |= cefpython.EVENTFLAG_SHIFT_DOWN
        if "ctrl" in modifiers:
            cefModifiers |= cefpython.EVENTFLAG_CONTROL_DOWN
        if "alt" in modifiers:
            cefModifiers |= cefpython.EVENTFLAG_ALT_DOWN
        if "capslock" in modifiers:
            cefModifiers |= cefpython.EVENTFLAG_CAPS_LOCK_ON
        # print("on_key_down(): cefModifiers = %s" % cefModifiers)
        cef_keycode = self.translate_to_cef_keycode(keycode[0])
        keyEvent = {
                "type": cefpython.KEYEVENT_RAWKEYDOWN,
                "native_key_code": cef_keycode,
                "modifiers": cefModifiers
                }
        # print("keydown keyEvent: %s" % keyEvent)
        self.browser.SendKeyEvent(keyEvent)
        if keycode[0] == 304:
            self.is_shift1 = True
        elif keycode[0] == 303:
            self.is_shift2 = True
        elif keycode[0] == 306:
            self.is_ctrl1 = True
        elif keycode[0] == 305:
            self.is_ctrl2 = True
        elif keycode[0] == 308:
            self.is_alt1 = True
        elif keycode[0] == 313:
            self.is_alt2 = True


    def on_key_up(self, keyboard, keycode):
        # print("on_key_up(): keycode = %s" % (keycode,))
        cefModifiers = cefpython.EVENTFLAG_NONE
        if self.is_shift1 or self.is_shift2:
            cefModifiers |= cefpython.EVENTFLAG_SHIFT_DOWN
        if self.is_ctrl1 or self.is_ctrl2:
            cefModifiers |= cefpython.EVENTFLAG_CONTROL_DOWN
        if self.is_alt1:
            cefModifiers |= cefpython.EVENTFLAG_ALT_DOWN
        # Capslock todo.
        cef_keycode = self.translate_to_cef_keycode(keycode[0])
        keyEvent = {
                "type": cefpython.KEYEVENT_KEYUP,
                "native_key_code": cef_keycode,
                "modifiers": cefModifiers
                }
        # print("keyup keyEvent: %s" % keyEvent)
        self.browser.SendKeyEvent(keyEvent)
        keyEvent = {
                "type": cefpython.KEYEVENT_CHAR,
                "native_key_code": cef_keycode,
                "modifiers": cefModifiers
                }
        # print("char keyEvent: %s" % keyEvent)
        self.browser.SendKeyEvent(keyEvent)
        if keycode[0] == 304:
            self.is_shift1 = False
        elif keycode[0] == 303:
            self.is_shift2 = False
        elif keycode[0] == 306:
            self.is_ctrl1 = False
        elif keycode[0] == 305:
            self.is_ctrl2 = False
        elif keycode[0] == 308:
            self.is_alt1 = False
        elif keycode[0] == 313:
            self.is_alt2 = False


    def translate_to_cef_keycode(self, keycode):
        # TODO: this works on Linux, but on Windows the key
        #       mappings will probably be different.
        # TODO: what if the Kivy keyboard layout is changed 
        #       from qwerty to azerty? (F1 > options..)
        cef_keycode = keycode
        if self.is_alt2:
            # The key mappings here for right alt were tested
            # with the utf-8 charset on a webpage. If the charset
            # is different there is a chance they won't work correctly.
            alt2_map = {
                    # tilde
                    "96":172,
                    # 0-9 (48..57)
                    "48":125, "49":185, "50":178, "51":179, "52":188, 
                    "53":189, "54":190, "55":123, "56":91, "57":93,
                    # minus
                    "45":92,
                    # a-z (97..122)
                    "97":433, "98":2771, "99":486, "100":240, "101":490,
                    "102":496, "103":959, "104":689, "105":2301, "106":65121,
                    "107":930, "108":435, "109":181, "110":497, "111":243,
                    "112":254, "113":64, "114":182, "115":438, "116":956,
                    "117":2302, "118":2770, "119":435, "120":444, "121":2299,
                    "122":447,
                    }
            if str(keycode) in alt2_map:
                cef_keycode = alt2_map[str(keycode)]
            else:
                print("Kivy to CEF key mapping not found (right alt), " \
                        "key code = %s" % keycode)
            shift_alt2_map = {
                    # tilde
                    "96":172,
                    # 0-9 (48..57)
                    "48":176, "49":161, "50":2755, "51":163, "52":36, 
                    "53":2756, "54":2757, "55":2758, "56":2761, "57":177,
                    # minus
                    "45":191,
                    # A-Z (97..122)
                    "97":417, "98":2769, "99":454, "100":208, "101":458,
                    "102":170, "103":957, "104":673, "105":697, "106":65122,
                    "107":38, "108":419, "109":186, "110":465, "111":211,
                    "112":222, "113":2009, "114":174, "115":422, "116":940,
                    "117":2300, "118":2768, "119":419, "120":428, "121":165,
                    "122":431,
                    # special: <>?  :"  {}
                    "44":215, "46":247, "47":65110,
                    "59":65113, "39":65114,
                    "91":65112, "93":65108,
                    }
            if self.is_shift1 or self.is_shift2:
                if str(keycode) in shift_alt2_map:
                    cef_keycode = shift_alt2_map[str(keycode)]
                else:
                    print("Kivy to CEF key mapping not found " \
                            "(shift + right alt), key code = %s" % keycode)
        elif self.is_shift1 or self.is_shift2:
            shift_map = {
                    # tilde
                    "96":126,
                    # 0-9 (48..57)
                    "48":41, "49":33, "50":64, "51":35, "52":36, "53":37,
                    "54":94, "55":38, "56":42, "57":40,
                    # minus, plus
                    "45":95, "61":43,
                    # a-z (97..122)
                    "97":65, "98":66, "99":67, "100":68, "101":69, "102":70,
                    "103":71, "104":72, "105":73, "106":74, "107":75, "108":76,
                    "109":77, "110":78, "111":79, "112":80, "113":81, "114":82,
                    "115":83, "116":84, "117":85, "118":86, "119":87, "120":88,
                    "121":89, "122":90,
                    # special: <>?  :"  {}
                    "44":60, "46":62, "47":63,
                    "59":58, "39":34,
                    "91":123, "93":125,
            }
            if str(keycode) in shift_map:
                cef_keycode = shift_map[str(keycode)]
        # Other keys:
        other_keys_map = {
            # Escape
            "27":65307,
            # F1-F12
            "282":65470, "283":65471, "284":65472, "285":65473,
            "286":65474, "287":65475, "288":65476, "289":65477,
            "290":65478, "291":65479, "292":65480, "293":65481,
            # Tab
            "9":65289,
            # Left Shift, Right Shift
            "304":65505, "303":65506,
            # Left Ctrl, Right Ctrl
            "306":65507, "305": 65508,
            # Left Alt, Right Alt
            "308":65513, "313":65027,
            # Backspace
            "8":65288,
            # Enter
            "13":65293,
            # PrScr, ScrLck, Pause
            "316":65377, "302":65300, "19":65299,
            # Insert, Delete, 
            # Home, End, 
            # Pgup, Pgdn
            "277":65379, "127":65535, 
            "278":65360, "279":65367,
            "280":65365, "281":65366,
            # Arrows (left, up, right, down)
            "276":65361, "273":65362, "275":65363, "274":65364,
        }
        if str(keycode) in other_keys_map:
            cef_keycode = other_keys_map[str(keycode)]
        return cef_keycode


    def go_forward(self):
        '''Going to forward in browser history
        '''
        print ("go forward")
        self.browser.GoForward()
    
    
    def go_back(self):
        '''Going back in browser history
        '''
        print ("go back")
        self.browser.GoBack()
    
    
    def on_touch_down(self, touch, *kwargs):
        if not self.collide_point(*touch.pos):
            return
        touch.grab(self)
        touch.moving = False
        self.touches.append(touch)
        if len(self.touches)==1:
            y = self.height-touch.pos[1]
            self.browser.SendMouseClickEvent(touch.x, y, cefpython.MOUSEBUTTON_LEFT,
                                             mouseUp=False, clickCount=1)
    
    
    def on_touch_move(self, touch, *kwargs):
        if touch.grab_current is not self:
            return
        
        if len(self.touches)==1:
            if (touch.dx>5 or touch.dy>5) or touch.moving:
                touch.moving = True
                y = self.height-touch.pos[1]
                self.browser.SendMouseMoveEvent(touch.x, y, mouseLeave=False)
        else:
            touch1, touch2 = self.touches[:2]
            dx = touch2.dx / 2. + touch1.dx / 2.
            dy = touch2.dy / 2. + touch1.dy / 2.
            self.browser.SendMouseWheelEvent(touch.x, self.height-touch.pos[1], dx, -dy)
        
        
    def on_touch_up(self, touch, *kwargs):
        if touch.grab_current is not self:
            return
        
        y = self.height-touch.pos[1]
        self.browser.SendMouseClickEvent(touch.x, y, cefpython.MOUSEBUTTON_LEFT,
                                         mouseUp=True, clickCount=1)
        self.touches.remove(touch)
        touch.ungrab(self)


class ClientHandler:

    _reset_js_bindings = False

    def __init__(self, browserWidget):
        self.browserWidget = browserWidget


    def _fix_select_boxes(self, frame):
        # See: http://marcj.github.io/jquery-selectBox/
        # Cannot use "file://" urls to load local resources, error:
        # | Not allowed to load local resource
        print("_fix_select_boxes()")
        resources_dir = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "kivy-select-boxes")
        js_file = os.path.join(resources_dir, "kivy-selectBox.js")
        js_content = ""
        with open(js_file, "r") as myfile:
            js_content = myfile.read()
        css_file = os.path.join(resources_dir, "kivy-selectBox.css")
        css_content = ""
        with open(css_file, "r") as myfile:
            css_content = myfile.read()
        css_content = css_content.replace("\r", "")
        css_content = css_content.replace("\n", "")
        jsCode = """
            %(js_content)s
            var head = document.getElementsByTagName('head')[0];
            var style = document.createElement('style');
            style.type = 'text/css';
            style.appendChild(document.createTextNode("%(css_content)s"));
            head.appendChild(style);
        """ % locals()
        frame.ExecuteJavascript(jsCode, 
                "kivy_.py > ClientHandler > OnLoadStart > _fix_select_boxes()")


    def OnLoadStart(self, browser, frame):
        self._fix_select_boxes(frame);
        browserWidget = browser.GetUserData("browserWidget")
        if browserWidget and browserWidget.keyboard_mode == "local":
            print("OnLoadStart(): injecting focus listeners for text controls")
            # The logic is similar to the one found in kivy-berkelium:
            # https://github.com/kivy/kivy-berkelium/blob/master/berkelium/__init__.py
            jsCode = """
                var __kivy__keyboard_requested = false;
                function __kivy__keyboard_interval() {
                    var element = document.activeElement;
                    if (!element) {
                        return;
                    }
                    var tag = element.tagName;
                    var type = element.type;
                    if (tag == "INPUT" && (type == "" || type == "text" 
                            || type == "password" || type == "email") || tag == "TEXTAREA") {
                        if (!__kivy__keyboard_requested) {
                            __kivy__request_keyboard();
                            __kivy__keyboard_requested = true;
                        }
                        return;
                    }
                    if (__kivy__keyboard_requested) {
                        __kivy__release_keyboard();
                        __kivy__keyboard_requested = false;
                    }
                }
                function __kivy__on_escape() {
                    if (document.activeElement) {
                        document.activeElement.blur();
                    }
                    if (__kivy__keyboard_requested) {
                        __kivy__release_keyboard();
                        __kivy__keyboard_requested = false;
                    }
                }
                setInterval(__kivy__keyboard_interval, 100);
            """
            frame.ExecuteJavascript(jsCode, 
                    "kivy_.py > ClientHandler > OnLoadStart")


    def OnLoadEnd(self, browser, frame, httpStatusCode):
        # Browser lost its focus after the LoadURL() and the 
        # OnBrowserDestroyed() callback bug. When keyboard mode
        # is local the fix is in the request_keyboard() method.
        # Call it from OnLoadEnd only when keyboard mode is global.
        browserWidget = browser.GetUserData("browserWidget")
        if browserWidget and browserWidget.keyboard_mode == "global":
            browser.SendFocusEvent(True)

    
    def OnLoadingStateChange(self, browser, isLoading, canGoBack,
            canGoForward):
        print("OnLoadingStateChange(): isLoading = %s" % isLoading)
        self.browserWidget.is_loading=isLoading
        browserWidget = browser.GetUserData("browserWidget")
        if self._reset_js_bindings and not isLoading:
            if browserWidget:
                browserWidget.set_js_bindings()
        if isLoading and browserWidget \
                and browserWidget.keyboard_mode == "local":
            # Release keyboard when navigating to a new page.
            #browserWidget.release_keyboard()
            pass
    
    
    def OnAddressChange(self, browser, frame, url):
        self.browserWidget.url = url

    
    def OnPaint(self, browser, paintElementType, dirtyRects, buffer, width, 
            height):        
        # print "OnPaint()"
        if paintElementType != cefpython.PET_VIEW:
            print ("Popups aren't implemented yet")
            return
        
        #update buffer
        buffer = buffer.GetString(mode="bgra", origin="top-left")
        
        #update texture of canvas rectangle
        self.browserWidget.texture.blit_buffer(buffer, colorfmt='bgra', 
                bufferfmt='ubyte')
        self.browserWidget._update_rect()
                
        return True
    

    def GetViewRect(self, browser, rect):
        width, height = self.browserWidget.texture.size
        rect.append(0)
        rect.append(0)
        rect.append(width)
        rect.append(height)
        # print("GetViewRect(): %s x %s" % (width, height))
        return True

class SupremeBot(App):
    def build(self):
        return CefBrowser()
        
if __name__ == "__main__":
    SupremeBot().run()