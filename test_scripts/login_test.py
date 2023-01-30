
import time

from demo_repository.pages.login_page import LoginPage
from demo_repository.test_scripts.base_test import BaseTest
def test_login():
    base=BaseTest()
    driver=base.start_browser("Chrome",'https://demo.actitime.com')
    login=LoginPage(driver)
    home=login.nevigate_to_home_page('admin','manager')
    time.sleep(5)
    home.click_on_logout()
    base.stop_browser()