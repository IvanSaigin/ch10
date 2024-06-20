from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage
import time

class Challenging_DOM(BasePage):

    

    CLICK_FOO = (By.CSS_SELECTOR, "#cefd2830-1161-013d-a454-4a518a7cafb9")
    CHEK_CANVAS = (By.CSS_SELECTOR, "#canvas")
    CLICK_Drag_and_Drop = (By.CSS_SELECTOR, "#content > ul > li:nth-child(5) > a")

    def challenging_DOM(self):


        self.element(self.CLICK_Drag_and_Drop).click()

        first = self.element(self.CHEK_CANVAS).text
        self.element(self.CLICK_FOO).click()
        second = self.element(self.CHEK_CANVAS).text
        
        return first,second