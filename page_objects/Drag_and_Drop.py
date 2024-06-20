from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage
import time

class Drag_and_Drop(BasePage):

    CLICK_Drag_and_Drop = (By.CSS_SELECTOR, "#content > ul > li:nth-child(10) > a")
    
    CLICK_left_scuare = (By.CSS_SELECTOR, "#column-a")
    CLICK_right_scuare = (By.CSS_SELECTOR, "#column-b")

    SELECTED_left_scuare = (By.CSS_SELECTOR, "#column-a > header")

    def drag_and_drop(self):


        self.element(self.CLICK_Drag_and_Drop).click()
        first_name_scuare = self.element(self.SELECTED_left_scuare).text

        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(self.CLICK_left_scuare, self.CLICK_right_scuare).perform()

        second_name_scuare = self.element(self.SELECTED_left_scuare).text
        
        return first_name_scuare,second_name_scuare