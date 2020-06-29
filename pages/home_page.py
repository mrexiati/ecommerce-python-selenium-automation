import utilities.custom_logger as cl
import logging
from base.basepage import BasePage



class HomeNavigation(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.homePage_locators = self.pageLocators('HomePage')

    def go_to_woman_product_page(self):
       self.elementClick(*self.locator(self.homePage_locators, 'woman_pro'))


    def go_to_cart_summary_page(self):
        self.elementClick(*self.locator(self.homePage_locators, 'home_to_cart'))






