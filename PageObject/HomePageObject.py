from selenium import common
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest


class HomePageObject:
    def __init__(self, driver):
        self.driver = driver

    def getGenderDropdown(self):
        return WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,'exampleFormControlSelect1')))
