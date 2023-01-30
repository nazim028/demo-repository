from selenium.webdriver.common.by import By
# from POM.AdvancePom.pages.base_page import BasePage
# from POM.AdvancePom.pages.home_page import HomePage
from demo_repository.pages.base_page import BasePage
from demo_repository.pages.home_page import HomePage


class LoginPage(BasePage):
    __username=lambda self:self.find_element(By.ID,"username")
    __password = lambda self: self.find_element(By.NAME,"pwd")
    __login_button = lambda self: self.find_element(By.ID,"loginButton")

    def nevigate_to_home_page(self,username,password):
        self.__username().send_keys(username)
        self.__password().send_keys(password)
        self.__login_button().click()

        return HomePage(self.driver)
