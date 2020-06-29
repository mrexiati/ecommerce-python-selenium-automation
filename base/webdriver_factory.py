from selenium import webdriver
import os
import test_data.testData as td


class WebDriverFactory:

    def __init__(self):
        """
        Inits WebDriverFactory class
        :Returns None:
        """
        self.browser = td.testData("browser")
        self.baseUrl = td.testData("environment")

    def getWebDriverInstance(self):
        """
        Get WebDriver Instance based on the browser configuration

        :return 'WebDriver Instance':
        """

        if self.browser == "firefox":
            # Set Firefox driver
            driverLocation = "../ArcherDX_coding_task/drivers/geckodriver "
            driver = webdriver.Firefox(driverLocation)

        elif self.browser == "chrome":
            # Set Chrome driver
            driverLocation = "../ArcherDX_coding_task/drivers/chromedriver "
            os.environ["webdriver.chrome.driver"] = driverLocation
            driver = webdriver.Chrome(driverLocation)


        else:
            driver = webdriver.Firefox()


        driver.implicitly_wait(15)
        driver.delete_all_cookies()
        driver.maximize_window()
        driver.get(self.baseUrl)

        return driver


