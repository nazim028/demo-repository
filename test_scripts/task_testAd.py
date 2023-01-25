import pytest

from POM.AdvancePom.pages.login_page import LoginPage
from POM.AdvancePom.test_scripts.base_test import BaseTest
from POM.AdvancePom.utilities import testdata
class Test_popup:
    @pytest.mark.parametrize('user,passwd',testdata.read_data_from_excel('D:\\selenium_framework\\POM\\AdvancePom\\testdata\\demodata.xlsx','Sheet1'))
    #@pytest.mark.parametrize('user,passwd', [('admin', 'manager'), ('trainee', 'trainee')])
    def test_popup(self,user,passwd):
        base=BaseTest()
        driver=base.start_browser("Chrome",'https://demo.actitime.com')
        login=LoginPage(driver)
        home=login.nevigate_to_home_page(user,passwd)
        task=home.navigate_to_task_tab()
        task.navigate_to_new_task_popup()
        home.click_on_logout()
        base.stop_browser()