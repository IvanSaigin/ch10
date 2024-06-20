from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.BasePage import BasePage
import time

class Context_Menu(BasePage):

    CLICK_Context_Menu = (By.CSS_SELECTOR, "#content > ul > li:nth-child(7) > a")
    
    CLICK_dotted_square = (By.CSS_SELECTOR, "#hot-spot")

    def context_menu(self):


        self.element(self.CLICK_Context_Menu).click()

        ActionChains(self.driver)\
        .click_and_hold(self.CLICK_dotted_square)\
        .perform()



        wait = WebDriverWait(self.driver, timeout=2)
        alert = wait.until(lambda d : d.switch_to.alert)
        text = alert.text
        alert.accept()

        return text


