from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time



class CartSummary(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.cart_summary_locators = self.pageLocators('CartSummary')

    def get_multi_quantity(self):
        pro_name = self.waitForElement(*self.locator(self.cart_summary_locators, 'first_info'))
        return pro_name.text

    def get_multi_price(self):
        pro_name = self.waitForElement(*self.locator(self.cart_summary_locators, 'multi_price'))
        return pro_name.text

    def click_remove_button(self):
        self.elementClick(*self.locator(self.cart_summary_locators, 'remove_button'))
        time.sleep(1)

    def remove_all(self):
        self.elementClick(*self.locator(self.cart_summary_locators, 'remove_button'))
        time.sleep(2)
        self.elementClick(*self.locator(self.cart_summary_locators, 'remove_button'))
        time.sleep(1)

    def empty_message(self):
        empty_message = self.waitForElement(*self.locator(self.cart_summary_locators, 'empty_message'))
        return empty_message.text

    def click_increase_button(self):
        self.elementClick(*self.locator(self.cart_summary_locators, 'increase'))
        time.sleep(1)

    def click_decrease_button(self):
        self.elementClick(*self.locator(self.cart_summary_locators, 'decrease'))
        time.sleep(1)









