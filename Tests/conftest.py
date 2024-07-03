import pytest
from selenium import webdriver



@pytest.fixture(scope='class')

def setup(request):
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()


@pytest.fixture(scope="class")
def startup(request):
    driver=webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()


