import pytest

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
@pytest.fixture(scope='class',autouse=True)
def tc_setup(browser,url):
    if browser=='chrome':
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser=='firefox':
        driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        print('provide valid browser')
    driver.implicitly_wait(30)
    driver.get(url)
    yield
    print('logoff')
    print('close browser')

def pytest_addoption(parser):
    parser.addoption('--browser')


@pytest.fixture(scope='session',autouse=True)
def browser(request):
    return request.config.getoption('--browser')


    # "C:\\chromeD\\chromedriver.exe"



