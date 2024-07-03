from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class MainWindow:

    def __init__(self,driver):
        self.driver=driver


    def childwindowlink(self):
        return  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT,"Click Here")))


    def mainWinHeader(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME,"h3")))