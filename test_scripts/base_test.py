from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
class BaseTest:
     def __int__(self):
         self.driver=None

     def start_browser(self,browser_name,url):
         if browser_name=="Chrome":
             self.driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
         elif browser_name=='Firefox':
             self.driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
         else:
             print('plz provide valid browser')
         self.driver.implicitly_wait(30)
         self.driver.maximize_window()
         self.driver.get(url)
         return self.driver

     def stop_browser(self):
         self.driver.quit()

#"C:\\chromeD\\chromedriver.exe"