from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage
import time

class Dropdown(BasePage):

    CLICK_Dropdown = (By.CSS_SELECTOR, "#content > ul > li:nth-child(11) > a")
    
    CLICK_dropdown_menu = (By.CSS_SELECTOR, "#dropdown")
    SELECTED_dropdown_menu = (By.CSS_SELECTOR, "#dropdown [selected]")
    CLICK_Dropdown_option = (By.CSS_SELECTOR, "#dropdown > option:nth-child(2)")

    def dropdown(self):


        self.element(self.CLICK_Dropdown).click()
        first = self.element(self.SELECTED_dropdown_menu).text
        self.element(self.CLICK_dropdown_menu).click()
        self.element(self.CLICK_Dropdown_option).click()

        second = self.element(self.SELECTED_dropdown_menu).text
        driver.quit()
        
        return first,second