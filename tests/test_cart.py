from pages.home_page import HomeNavigation
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.cart_summary import CartSummary
import unittest
import pytest
import sys
import allure
import test_data.testData as td
import time

sys.path.insert(0, '../..')


@pytest.mark.usefixtures("setUp", "oneTimeSetUp")
class CartTest(unittest.TestCase):

    first_item_name = td.testData("firstProductName")
    first_item_quantity = td.testData("firstProductQuantity")
    first_size = td.testData("firstProductSize")
    first_color = td.testData("firstProductColor")
    first_color_size = td.testData("firstProColorAndSize")
    first_total = td.testData("firstTotal")

    second_item_name = td.testData("secondProductName")
    second_item_quantity = td.testData("secondProductQuantity")
    second_size = td.testData("secondProductSize")
    second_color = td.testData("secondProductColor")

    multiple_quantity = td.testData("firstMultipleInfo")
    multiple_price = td.testData("multiPrice")
    same_multiple_price = td.testData("sameMultiPrice")

    decreased_quantity = td.testData("decreasedNumber")
    decreased_price = td.testData("decreasedPrice")
    empty_message = td.testData("emptyMessage")



    succes_message = td.testData("successMessage")

    lower_boundary_quantity = td.testData("lowerBoundary")
    lower_boundary_message = td.testData("lowerBoundaryMessage")
    upper_boundary_quantity = td.testData("upperBoundary")
    upper_boundary_message = td.testData("upperBoundaryMessage")

    before_quantity = td.testData("beforeIncrease")
    increased_quantity = td.testData("increased")
    after_total = td.testData("afterTotal")
    navigate_back = td.testData("navigateBack")

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.homeNavigation = HomeNavigation(self.driver)
        self.productPage = ProductPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.cart_summary = CartSummary(self.driver)

    @pytest.mark.skip
    def test_add_one_item(self):
            self.homeNavigation.go_to_woman_product_page()
            self.productPage.select_a_product(self.first_item_name)
            self.cart_page.enter_product_info(quantity=self.first_item_quantity, size=self.first_size, color=self.first_color)

            self.assertEqual(self.succes_message, self.cart_page.obtain_message())
            self.assertEqual(self.first_item_name, self.cart_page.obtain_product_name())
            self.assertEqual(self.first_color_size, self.cart_page.obtain_color_size())
            self.assertEqual(self.first_item_quantity, self.cart_page.obtain_cart_quantity())
            self.assertEqual(self.first_total, self.cart_page.obtain_total_price())
            self.driver.delete_all_cookies()

    @pytest.mark.skip
    def test_add_multiple_items(self):
        self.homeNavigation.go_to_woman_product_page()
        self.productPage.select_a_product(self.first_item_name)
        self.cart_page.enter_product_info(quantity=self.first_item_quantity, size=self.first_size, color=self.first_color)
        self.assertEqual(self.succes_message, self.cart_page.obtain_message())

        self.cart_page.continue_shopping()

        self.productPage.select_a_product(self.second_item_name)
        self.cart_page.enter_product_info(quantity=self.second_item_quantity, size=self.second_size, color=self.second_color)
        self.assertEqual(self.succes_message, self.cart_page.obtain_message())
        self.cart_page.go_to_cart_summary()

        self.assertEqual(self.multiple_quantity, self.cart_summary.get_multi_quantity())
        self.assertEqual(self.multiple_price, self.cart_summary.get_multi_price())

        self.driver.delete_all_cookies()

    @pytest.mark.skip
    def test_add_same_item_multiple_times(self):
        self.homeNavigation.go_to_woman_product_page()
        self.productPage.select_a_product(self.first_item_name)
        self.cart_page.enter_product_info(quantity=self.first_item_quantity, size=self.first_size,color=self.first_color)
        self.assertEqual(self.succes_message, self.cart_page.obtain_message())

        self.cart_page.continue_shopping()

        self.productPage.select_a_product(self.first_item_name)
        self.cart_page.enter_product_info(quantity=self.first_item_quantity, size=self.first_size,color=self.first_color)
        self.assertEqual(self.succes_message, self.cart_page.obtain_message())
        self.cart_page.go_to_cart_summary()

        self.assertEqual(self.multiple_quantity, self.cart_summary.get_multi_quantity())
        self.assertEqual(self.same_multiple_price, self.cart_summary.get_multi_price())

        self.driver.delete_all_cookies()

    @pytest.mark.skip
    def test_remove_one_item_from_multiple_items(self):
        self.homeNavigation.go_to_woman_product_page()
        self.productPage.select_a_product(self.first_item_name)
        self.cart_page.enter_product_info(quantity=self.first_item_quantity, size=self.first_size,color=self.first_color)
        self.assertEqual(self.succes_message, self.cart_page.obtain_message())

        self.cart_page.continue_shopping()

        self.productPage.select_a_product(self.second_item_name)
        self.cart_page.enter_product_info(quantity=self.second_item_quantity, size=self.second_size, color=self.second_color)
        self.assertEqual(self.succes_message, self.cart_page.obtain_message())
        self.cart_page.go_to_cart_summary()

        self.assertEqual(self.multiple_quantity, self.cart_summary.get_multi_quantity())
        self.assertEqual(self.multiple_price, self.cart_summary.get_multi_price())

        self.cart_summary.click_remove_button()
        self.assertEqual(self.decreased_quantity,self.cart_summary.get_multi_quantity())
        self.assertEqual(self.decreased_price,self.cart_summary.get_multi_price())

        self.driver.delete_all_cookies()

    @pytest.mark.skip
    def test_remove_all_items(self):
        self.homeNavigation.go_to_woman_product_page()
        self.productPage.select_a_product(self.first_item_name)
        self.cart_page.enter_product_info(quantity=self.first_item_quantity, size=self.first_size,
                                          color=self.first_color)
        self.assertEqual(self.succes_message, self.cart_page.obtain_message())

        self.cart_page.continue_shopping()

        self.productPage.select_a_product(self.second_item_name)
        self.cart_page.enter_product_info(quantity=self.second_item_quantity, size=self.second_size,
                                          color=self.second_color)
        self.assertEqual(self.succes_message, self.cart_page.obtain_message())
        self.cart_page.go_to_cart_summary()

        self.assertEqual(self.multiple_quantity, self.cart_summary.get_multi_quantity())
        self.assertEqual(self.multiple_price, self.cart_summary.get_multi_price())

        self.cart_summary.remove_all()
        self.assertEqual(self.empty_message, self.cart_summary.empty_message())

        self.driver.delete_all_cookies()

    @pytest.mark.skip
    def test_cart_quantity_lower_boundary(self):
        self.homeNavigation.go_to_woman_product_page()
        self.productPage.select_a_product(self.first_item_name)
        self.cart_page.enter_product_info(quantity=self.lower_boundary_quantity, size=self.first_size,color=self.first_color)

        self.assertEqual(self.lower_boundary_message, self.cart_page.null_quantity())

        self.driver.delete_all_cookies()

    @pytest.mark.skip
    def test_cart_quantity_upper_boundary(self):
        self.homeNavigation.go_to_woman_product_page()
        self.productPage.select_a_product(self.first_item_name)
        self.cart_page.enter_product_info(quantity=self.upper_boundary_quantity, size=self.first_size,color=self.first_color)

        self.assertEqual(self.upper_boundary_message, self.cart_page.null_quantity())

        self.driver.delete_all_cookies()

    @pytest.mark.skip
    def test_increase_item_quantity(self):
        self.homeNavigation.go_to_woman_product_page()
        self.productPage.select_a_product(self.first_item_name)
        self.cart_page.enter_product_info(quantity=self.first_item_quantity, size=self.first_size,color=self.first_color)
        self.cart_page.continue_checkout()

        self.assertEqual(self.before_quantity, self.cart_summary.get_multi_quantity())
        self.assertEqual(self.first_total, self.cart_summary.get_multi_price())

        self.cart_summary.click_increase_button()

        self.assertEqual(self.increased_quantity, self.cart_summary.get_multi_quantity())
        self.assertEqual(self.after_total, self.cart_summary.get_multi_price())

        self.driver.delete_all_cookies()

    @pytest.mark.skip
    def test_decrease_item_quantity(self):
        self.homeNavigation.go_to_woman_product_page()
        self.productPage.select_a_product(self.first_item_name)
        self.cart_page.enter_product_info(quantity=self.first_item_quantity, size=self.first_size,color=self.first_color)
        self.cart_page.continue_checkout()

        self.assertEqual(self.before_quantity, self.cart_summary.get_multi_quantity())
        self.assertEqual(self.first_total, self.cart_summary.get_multi_price())

        self.cart_summary.click_decrease_button()
        self.assertEqual(self.empty_message, self.cart_summary.empty_message())

        self.driver.delete_all_cookies()

    def test_cart_cash_function(self):
        self.homeNavigation.go_to_woman_product_page()
        self.productPage.select_a_product(self.first_item_name)
        self.cart_page.enter_product_info(quantity=self.first_item_quantity, size=self.first_size, color=self.first_color)
        self.cart_page.open_new_tab_navigate_to_other_page()

        self.homeNavigation.go_to_cart_summary_page()

        self.assertEqual(self.navigate_back, self.cart_summary.get_multi_quantity())
        self.assertEqual(self.first_total, self.cart_summary.get_multi_price())

        time.sleep(5)































