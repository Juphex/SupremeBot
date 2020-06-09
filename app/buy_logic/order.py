#from jnius import autoclass, cast
#from android.runnable import run_on_ui_thread

# activity = autoclass("org.kivy.android.PythonActivity").mActivity
# context = cast("android.content.Context", activity.getApplicationContext())
# WV = autoclass("android.webkit.WebView")
# WVC = autoclass("com.my.webview.MyWebViewClient")
# ChromeClient = autoclass("android.webkit.WebChromeClient")
from kivy.app import App
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


class Order:

    #For Android
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
    '''Buys an item using the selenium webdriver.
        Given a specific item, size and the chromedriver'''
    @staticmethod
    def buy(item, sizes, driver):
        success = False
        tee_size = sizes[0]
        shorts_size = sizes[1]
        url = item.link
        driver.get(url)

        #some buttons may have not been occured
        wait = WebDriverWait(driver, 10)

        try:
            select = Select(driver.find_element_by_css_selector("select#size"))
            success = Order.select_size(select, tee_size=tee_size, shorts_size=shorts_size)

        except NoSuchElementException:
            # case item has no sizes
            # move on with following code
            pass

        driver.find_element_by_css_selector("input.button[value='hinzufügen']").click()
        sleep(1)
        checkout_btn_selector = "a.button.checkout"
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,checkout_btn_selector)))
        driver.find_element_by_css_selector(checkout_btn_selector).click()

        ''' Adress and Payment details '''

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

    ''' Takes an Select object from selenium and selects the given size'''
    @staticmethod
    def select_size(select, tee_size, shorts_size):
        #try short and shirt sizes
        try:
            select.select_by_visible_text(tee_size)
        except NoSuchElementException:
            print("shirt size not found")
            print(tee_size)

            try:
                print("trying shorts size")
                print(shorts_size)
                select.select_by_visible_text(shorts_size)
            except NoSuchElementException:
                print("short size not found")
                return False

        return True