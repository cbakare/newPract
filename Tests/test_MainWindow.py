from selenium.webdriver.common.by import By

from PageObject.Object_Mainwindows import MainWindow
import pytest
import time


@pytest.mark.usefixtures("setup")
class Test_MainWinodw:


    def test_GetwdwHeader(self):
        Mwin = MainWindow(self.driver)
        header=Mwin.mainWinHeader()
        assert "Opening a new window"==header.text,  "Page did not load as expected "


    def test_OpenChildWin(self):
        Mwin=MainWindow(self.driver)
        Mwin.childwindowlink().click()
        windowhandles=self.driver.window_handles
        self.driver.switch_to.window(windowhandles[1])
        print(self.driver.find_element(By.TAG_NAME,"h3").text)
        self.driver.close()
        self.driver.switch_to.window(windowhandles[0])
        time.sleep(5)
        print(self.driver.find_element(By.TAG_NAME, "h3").text)




