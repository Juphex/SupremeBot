#from jnius import autoclass, cast
#from android.runnable import run_on_ui_thread

# activity = autoclass("org.kivy.android.PythonActivity").mActivity
# context = cast("android.content.Context", activity.getApplicationContext())
# WV = autoclass("android.webkit.WebView")
# WVC = autoclass("com.my.webview.MyWebViewClient")
# ChromeClient = autoclass("android.webkit.WebChromeClient")


class Order:

    # @run_on_ui_thread
    # def buy(item, size):
    #     #get settings
    #     webview = WV(activity)
    #     webview.getSettings().setJavaScriptEnabled(True)
    #     webview.setWebChromeClient(ChromeClient())
    #     wvc = WVC()
    #     #document.getElementById("mySelect").selectedIndex = 1;
    #     wvc.setScript("javascript:document.getElementByName('commit').click();")
    #     webview.setWebViewClient(wvc)
    #     activity.setContentView(webview)
    #     webview.loadUrl(item.link)

    def buy(item, size):
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options

        CHROMEDRIVER_PATH = '/chromedriver/chromedriver.exe'
        WINDOW_SIZE = "1024,768"

        chrome_options = Options()  
        chrome_options.add_argument("--headless")  
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        chrome_options.binary_location = CHROMEDRIVER_PATH

        driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                                chrome_options=chrome_options
                                )  
        driver.get("https://www.google.com")
        driver.get_screenshot_as_file("capture.png")
        driver.close()



