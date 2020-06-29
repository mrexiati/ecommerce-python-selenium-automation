from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time



class CartPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.cartPage_locators = self.pageLocators('CartPage')

    def enter_product_info(self, quantity, color, size):
        self.clearKeys(*self.locator(self.cartPage_locators, 'quantity'))
        self.sendKeys(quantity, *self.locator(self.cartPage_locators, 'quantity'))
        self.selectDropdown(size, *self.locator(self.cartPage_locators, 'size'))
        self.select_color(color)

        self.elementClick(*self.locator(self.cartPage_locators, 'add_to_cart'))

    def select_color(self, color):

        items = self.getElementListT(*self.locator(self.cartPage_locators, 'all_li'))
        for item in items:
            if item.get_attribute("name") == color:
                item.click()

    def null_quantity(self):
        message = self.getText(*self.locator(self.cartPage_locators, 'null_quantity'))
        return message


    def continue_checkout(self):
        self.elementClick(*self.locator(self.cartPage_locators, 'continue_checkout'))


    def obtain_message(self):
        message = self.getText(*self.locator(self.cartPage_locators, 'success_message'))
        return message

    def obtain_product_name(self):

        pro_name = self.waitForElement(*self.locator(self.cartPage_locators, 'pro_name'))
        return pro_name.text

    def obtain_color_size(self):

        color_size = self.waitForElement(*self.locator(self.cartPage_locators, 'color_size'))
        return color_size.text

    def obtain_cart_quantity(self):
        cart_quantity = self.waitForElement(*self.locator(self.cartPage_locators, 'cart_quantity'))
        return cart_quantity.text

    def obtain_total_price(self):
        total_price = self.waitForElement(*self.locator(self.cartPage_locators, 'total_price'))
        return total_price.text

    def continue_shopping(self):
        self.elementClick(*self.locator(self.cartPage_locators, 'continue_shopping'))
        self.pageBack()


    def go_to_cart_summary(self):
        self.elementClick(*self.locator(self.cartPage_locators, 'cart_sum'))

    def open_new_tab_navigate_to_other_page(self):
        self.driver.execute_script('''window.open("http://www.google.com","_blank");''')
        window_before = self.driver.window_handles[0]
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_before)
        time.sleep(1)
        self.driver.close()
        time.sleep(1)
        self.driver.switch_to_window(window_after)
        time.sleep(1)
        self.driver.get("http://automationpractice.com/index.php")

















