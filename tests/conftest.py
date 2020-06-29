import pytest
from base.webdriver_factory import WebDriverFactory



@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")




@pytest.fixture(scope="class")
def oneTimeSetUp(request):
    print("Running class setUp")
    wdf = WebDriverFactory()
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver


    yield driver




    print("Running class tearDown")
    driver.close()
    driver.quit()

