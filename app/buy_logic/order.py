from jnius import autoclass, cast
from android.runnable import run_on_ui_thread

activity = autoclass("org.kivy.android.PythonActivity").mActivity
context = cast("android.content.Context", activity.getApplicationContext())
WV = autoclass("android.webkit.WebView")
WVC = autoclass("com.my.webview.MyWebViewClient")
ChromeClient = autoclass("android.webkit.WebChromeClient")


class Order:

    @run_on_ui_thread
    def buy(item, size):
        #get settings
        webview = WV(activity)
        webview.getSettings().setJavaScriptEnabled(True)
        webview.setWebChromeClient(ChromeClient())
        wvc = WVC()
        #document.getElementById("mySelect").selectedIndex = 1;
        wvc.setScript("javascript:document.getElementByName('commit').click();")
        webview.setWebViewClient(wvc)
        activity.setContentView(webview)
        webview.loadUrl(item.link)
