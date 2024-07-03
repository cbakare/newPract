import pytest
from selenium.webdriver.support.select import Select

from PageObject.HomePageObject import  HomePageObject
import time


@pytest.mark.usefixtures("startup")
class Test_HomePage:

    def test_GenderDropdown(self):
        home=HomePageObject(self.driver)
        dropdown=Select(home.getGenderDropdown())
        dropdown.select_by_visible_text("Female")
        time.sleep(5)