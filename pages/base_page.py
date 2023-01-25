from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self,driver):
        self.driver=driver
        driver.set_page_load_timeout(15)

    __logout_link = lambda self:self.find_element(By.ID,"logoutLink")

    def find_element(self,locator_type,locator_value):
        try:
            element = self.driver.find_element(locator_type,locator_value)
            return element
        except NoSuchElementException:
            print('element is not present',NoSuchElementException)

    def click_on_logout(self):
        self.__logout_link().click()
