from POM.AdvancePom.pages.login_page import LoginPage
from POM.AdvancePom.test_scripts.base_test import BaseTest
import time
base=BaseTest()
driver=base.start_browser("Chrome",'https://demo.actitime.com')
login=LoginPage(driver)
home=login.nevigate_to_home_page('admin','manager')
time.sleep(5)
home.click_on_logout()
base.stop_browser()