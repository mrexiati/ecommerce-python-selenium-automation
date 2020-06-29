from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import time
import os
import allure



class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, resultMessage):
        """
        Take a screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() *1000)) + ".png"
        if len(fileName) >= 200:
            fileName = str(round(time.time() *1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            allure.attach(self.driver.get_screenshot_as_png(),
                          name=fileName,
                          attachment_type=allure.attachment_type.PNG)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()

    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type" + locatorType + "not correct/supported")
        return False

    def dropdownSelectElement(self, selector, locator="", locatorType="xpath", selectorType="value"):
        try:
            element = self.getElement(locator, locatorType)
            sel = Select(element)
            if selectorType == "value":
                sel.select_by_value(selector)
                time.sleep(1)
            elif selectorType == "index":
                sel.select_by_index(selector)
                time.sleep(1)
            elif selectorType == "text":
                sel.select_by_visible_text(selector)
                time.sleep(1)
            self.log.info("Element selected with selector: " + str(selector) +
                          " and selectorType: " + selectorType)

        except:
            self.log.error("Element not selected with selector: " + str(selector) +
                       " and selectorType: " + selectorType)
            print_stack()

    def getDropdownOptionsCount(self, locator, locatorType="id"):
        '''
        get the number of options of drop down list
        :return: number of Options of drop down list
        '''
        options = None
        try:
            element = self.getElement(locator, locatorType)
            sel = Select(element)
            options = sel.options
            self.log.info("Element found with locator: " + locator +
                          " and locatorType: " + locatorType)
        except:
            self.log.error("Element not found with locator: " + locator +
                       " and locatorType: " + locatorType)

        return options

    def getDropdownSelectedOptionText(self, locator, locatorType="id"):
        '''
        get the text of selected option in drop down list
        :return: the text of selected option in drop down list
        '''
        selectedOption_text = None
        try:
            element = self.getElement(locator, locatorType)
            sel = Select(element)
            selectedOption_text = sel.first_selected_option.text
            self.log.info("Return the selected option of drop down list with locator: " + locator +
                          " and locatorType: " + locatorType)
        except:
            self.log.error("Can not return the selected option of drop down list with locator: " + locator +
                       " and locatorType: " + locatorType)

        return selectedOption_text

    def getDropdownSelectedOptionValue(self, locator, locatorType="id"):
        '''
        get the value of selected option in drop down list
        :return: the value of selected option in drop down list
        '''
        selectedOption_value = None
        try:
            element = self.getElement(locator, locatorType)
            sel = Select(element)
            selectedOption_value = sel.first_selected_option.get_attribute("value")
            self.log.info("Return the selected option of drop down list with locator: " + locator +
                          " and locatorType: " + locatorType)
        except:
            self.log.error("Can not return the selected option of drop down list with locator: " + locator +
                       " and locatorType: " + locatorType)

        return selectedOption_value

    def getElement(self, locator, locatorType="xpath"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator +
                          " and locatorType: " + locatorType)
        except:
            self.log.error("Element not found with locator: " + locator +
                          " and locatorType: " + locatorType)
        return element

    def isElementSelected(self, locator, locatorType):
        isSelected = None
        try:
            element = self.getElement(locator, locatorType)
            isSelected = element.is_selected()
            self.log.info("Element found with locator: " + locator +
                          " and locatorType: " + locatorType)
        except:
            self.log.error("Element not found with locator: " + locator +
                           " and locatorType: " + locatorType)

        return isSelected

    def getElementList(self, locator, locatorType="xpath"):
        """
        Get list of elements
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator: " + locator +
                          " and locatorType: " + locatorType)
        except:
            self.log.error("Element list not found with locator: " + locator +
                           " and locatorType: " + locatorType)

        return element

    def getElementListT(self, locator, locatorType="xpath"):
        """
        Get elementList list for a provided locator
        Required Parameters:
            locator: locator of the element list to find
        Optional Parameters:
            locatorType: Type of the locator(id(default), xpath, css, classname, linktext)
        Returns:
            Element List
        """


        elementList = None
        try:
            locatorType = locatorType.lower()
            if locatorType == "id":
                elementList = self.driver.find_elements_by_id(locator)
            elif locatorType == "name":
                elementList = self.driver.find_elements_by_name(locator)
            elif locatorType == "xpath":
                elementList = self.driver.find_elements_by_xpath(locator)
            elif locatorType == "css":
                elementList = self.driver.find_elements_by_css_selector(locator)
            elif locatorType == "classname":
                elementList = self.driver.find_elements_by_class_name(locator)
            elif locatorType == "linktext":
                elementList = self.driver.find_elements_by_link_text(locator)
            elif locatorType == "tag":
                elementList = self.driver.find_elements_by_tag_name(locator)
            else:
                self.log.warning("Locator type " + locatorType + " not correct/supported")
            self.log.info("Element list found with locator :: " + locator)
        except :
            self.log.error("Element list not found with locator :: " + locator)
            print_stack()
        return elementList



    def elementClick(self, locator="", locatorType="xpath", element=None):
        """
        Either provide element or a combination of locator and locatorType
        """

        try:
            if locator:
                element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, locator)))
            element.click()
            self.log.info("clicked on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.error("cannot click on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()



    def elementHover(self, locator="", locatorType="id", element=None):
        """
        Either provide element or a combination of locator and locatorType
        """

        try:
            if locator:
                element = self.getElement(locator, locatorType)
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()
            time.sleep(2)
            self.log.info("hover to element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.error("cannot hover to the element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator="", locatorType="xpath", element=None):
        """
        Send keys to an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, locator)))
            element.send_keys(data)
            self.log.info("send data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.error("cannot send data on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()



    def clearKeys(self, locator="", locatorType="id", element=None):
        """
        Clear keys of an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, locator)))
            element.clear()
            self.log.info("Clear data of element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.error("cannot clear data of the element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()

    def getText(self, locator="", locatorType="xpath", element=None, info=""):
        """
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) !=0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text


    def isElementPresent(self, locator="", locatorType="id", element=None):
        """
        Check if element is present
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element found with locator: " + locator +
                              " and locatorType: " + locatorType)
                return True
            else:
                self.log.error("Element not found with locator: " + locator +
                              " and locatorType: " + locatorType)
                return False
        except:
            self.log.error("Element not found with locator: " + locator +
                              " and locatorType: " + locatorType)
            return False

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        """
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " and locatorType: " + locatorType)
            else:
                self.log.error("Element is not displayed with locator: " + locator +
                              " and locatorType: " + locatorType)
            return isDisplayed
        except:
            self.log.error("Element is not displayed with locator: " + locator +
                              " and locatorType: " + locatorType)
            return False

    def elementPresenceCheck(self, locator="", locatorType="id"):
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElement(self, locator, locatorType = 'xpath', timeout = 10, pollFrequency = 0.5 ):
        element = None
        try:
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")

            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            ByType = self.getByType(locatorType)
            element = wait.until(EC.element_to_be_clickable((ByType,locator)))

            self.log.info("Element appeared on the web page")

        except:
            self.log.info("Element not appeared on the web page")
            print_stack()

        return element

    def webScroll(self, direction="up"):
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")
        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def getURL(self):
        '''
        Get the current URL
        :return: current URL
        '''
        currentURL = self.driver.current_url

        return currentURL

    def pageBack(self):
        '''
        page back the browser
        '''
        self.driver.execute_script("window.history.go(-1)")
        self.driver.execute_script("window.history.go(-1)")

    def getAttributeValue(self, locator="", locatorType="id", element=None, attribute="value"):
        '''
        get attribute value
        '''
        try:
            if locator:
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            attribute_value = element.get_attribute(attribute)
        except:
            self.log.error("Failed to get " + attribute + " in element with locator: " +
                           locator + " and locatorType: " + locatorType)
            print_stack()
            attribute_value = None
        return attribute_value

    def refresh(self):
        self.driver.get(self.driver.current_url)

    def page_has_loaded(self):
        try:
            WebDriverWait(self.driver, 1000, poll_frequency=0.5).until(lambda driver: self.driver.execute_script('return document.readyState == "complete";'))
            WebDriverWait(self.driver, 1000, poll_frequency=0.5).until(lambda driver: self.driver.execute_script('return jQuery.active == 0'))
            WebDriverWait(self.driver, 1000, poll_frequency=0.5).until(lambda driver: self.driver.execute_script('return typeof jQuery != "undefined"'))
            WebDriverWait(self.driver, 1000, poll_frequency=0.5).until(lambda driver: self.driver.execute_script('return angular.element(document).injector().get("$http").pendingRequests.length === 0'))
        except:
            return False

    def selectDropdown(self, optionToSelect,locator="", locatorType="xpath",
                       byValue=True, byIndex=False, timeToWait=0):
        """
        Select option from a dropdown (default by visible text)
        Required Parameters:
            dropDownElement: Dropdown element
            optionToSelect: Option to select from the dropdown (Visible Text / Value / Index)
            info: Information about the optionToSelect, usually text on the optionToSelect
        Optional Parameters:
            byValue: Provide True if you want to select by value
            byIndex: Provide True if you want to select by index
            timeToWait: Time you want to wait after selecting the element
        Returns:
            None
        """
        try:
            element = self.getElement(locator, locatorType)
            select = Select(element)

            if byValue:
                select.select_by_value(optionToSelect)
            elif byIndex:
                select.select_by_index(optionToSelect)
            else:
                select.select_by_visible_text(optionToSelect)
            self.log.info("Selected option --> :: '" + optionToSelect + "' from dropdown:: '" + "'")
            self.log.info("Waiting after selecting the element for " + str(timeToWait) + " seconds")
            time.sleep(timeToWait)
            return True
        except:
            self.log.error("Could not select option --> :: '" + optionToSelect + "' from dropdown:: '" +"'")
            print_stack()
            return False







