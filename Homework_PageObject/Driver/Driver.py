
from selenium import webdriver
from  webdriver_manager.chrome import ChromeDriverManager


class Driver:
    """Create new webdriver."""
    # chrome_driver=webdriver.Chrome(executable_path="E:\pycharm\chromedriver_win32")
    chrome_driver=webdriver.Chrome(ChromeDriverManager().install())




