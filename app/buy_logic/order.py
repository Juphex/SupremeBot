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

    #multithread?
    @staticmethod
    def buy(item, size, driver):
        success = False

        url = item.link
        driver.get(url)
        from selenium.common.exceptions import NoSuchElementException
        from selenium.webdriver.support.ui import Select
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        import selenium.webdriver.support.expected_conditions as EC

        wait = WebDriverWait(driver, 10)
        select = Select(driver.find_element_by_css_selector("select#size"))

        try:
            select.select_by_visible_text(size)
        except NoSuchElementException:
            print("size not found")
            return success
        driver.find_element_by_css_selector("input.button[value='hinzufügen']").click()
        from time import sleep
        sleep(1)
        checkout_btn_selector = "a.button.checkout"
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,checkout_btn_selector)))
        driver.find_element_by_css_selector(checkout_btn_selector).click()

        ''' Adress and Payment details '''
        from kivy.app import App

        name, email, tel, street, street_nr, address_3, city, plz, country \
            = App.get_running_app().get_adress_details()
        credit_card_type, credit_card_nr, credit_card_exp_month, credit_card_exp_year, credit_card_cvv \
            = App.get_running_app().get_payment_deatils()

        driver.find_element_by_css_selector("#order_billing_name").send_keys(name)
        driver.find_element_by_css_selector("#order_email").send_keys(email)
        driver.find_element_by_css_selector("#order_tel").send_keys(tel)
        driver.find_element_by_css_selector("#bo").send_keys(street)
        driver.find_element_by_css_selector("input[id='oba3']").send_keys(street_nr)
        driver.find_element_by_css_selector("#order_billing_address_3").send_keys(address_3)
        driver.find_element_by_css_selector("#order_billing_city").send_keys(city)
        driver.find_element_by_css_selector("#order_billing_zip").send_keys(plz)

        select = Select(driver.find_element_by_css_selector("select#order_billing_country"))
        try:
            select.select_by_visible_text(country)
        except NoSuchElementException:
            print("billing country not found")
            return success

        select = Select(driver.find_element_by_css_selector("select#credit_card_type"))
        try:
            select.select_by_visible_text(credit_card_type)
        except NoSuchElementException:
            print("credit card type not found")
            return success

        driver.find_element_by_css_selector("#cnb").send_keys(credit_card_nr)

        select = Select(driver.find_element_by_css_selector("select#credit_card_month"))
        try:
            select.select_by_visible_text(credit_card_exp_month)
        except NoSuchElementException:
            print("credit card expiration month not found")
            return success

        select = Select(driver.find_element_by_css_selector("select#credit_card_year"))
        try:
            select.select_by_visible_text(credit_card_exp_year)
        except NoSuchElementException:
            print("credit card expiration year not found")
            return success

        driver.find_element_by_css_selector("#vval").send_keys(credit_card_cvv)
        driver.find_element_by_css_selector("label[class='has-checkbox terms'] > div > ins.iCheck-helper").click()
        driver.find_element_by_css_selector("#pay > input").click()

        success = True

        return success





