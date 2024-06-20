from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage
import time

class Dynamic_Loading(BasePage):

    CLICK_Dynamic_Loading = (By.CSS_SELECTOR, "#content > ul > li:nth-child(14) > a")
    
    CLICK_dynamic = (By.CSS_SELECTOR, "#content > div > a:nth-child(5)")
    CLICK_button = (By.CSS_SELECTOR, "#start > button")
    SELECTED_text = (By.CSS_SELECTOR, "#finish > h4")

    def dynamic_loading(self):


        self.element(self.CLICK_Dynamic_Loading).click()
        self.element(self.CLICK_dynamic).click()
        self.element(self.CLICK_button).click()
        time.sleep(8)

        text = self.element(self.SELECTED_text).text
        driver.quit()

        return text