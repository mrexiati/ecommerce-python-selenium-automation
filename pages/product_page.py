from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.productPage_locators = self.pageLocators('ProductPage')



    def select_a_product(self, pro_name):
        items = self.getElementListT(*self.locator(self.productPage_locators, 'all_pro'))
        for item in items:
            if item.get_attribute("title") == pro_name:
                time.sleep(1)
                item.click()
                break
