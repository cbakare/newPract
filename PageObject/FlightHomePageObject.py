from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class FlightHomePageObject:

    def __init__(self,driver):
        self.driver=driver

    def getCountrytypeahead(self):
        return WebDriverWait(self.driver,2).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='autosuggest']")))

    def getAllOptionsFromDD(self):
        return self.driver.find_elements(By.XPATH,'//li[@class="ui-menu-item"]/a')





