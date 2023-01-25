from selenium.webdriver.common.by import By
from time import sleep
from POM.AdvancePom.pages.base_page import BasePage

class TaskPage(BasePage):
    __add_new_button = lambda self:self.find_element(By.XPATH,"//div[contains(@class,'title ellipsis')]")
    __new_task_button = lambda self:self.find_element(By.XPATH,"//div[contains(@class,'item createNewTasks')]")
    __close_button = lambda self:self.find_element(By.XPATH,"//div[@id='closeCreateTasksPopupButton']")

    def navigate_to_new_task_popup(self):
        self.__add_new_button().click()
        self.__new_task_button().click()
        sleep(5)
        self.__close_button().click()
