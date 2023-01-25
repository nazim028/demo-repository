from selenium.webdriver.common.by import By
from POM.AdvancePom.pages.base_page import BasePage
from POM.AdvancePom.pages.task_page import TaskPage

class HomePage(BasePage):
    def __task_tab(self):return self.find_element(By.XPATH,"//*[@id='container_tasks']")

    def navigate_to_task_tab(self):
        self.__task_tab().click()

        return TaskPage(self.driver)