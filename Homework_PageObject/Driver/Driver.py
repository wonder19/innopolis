"""Contains all creations of webdrivers."""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Driver:
    """Create new Chrome webdriver."""
    chrome_driver=webdriver.Chrome(ChromeDriverManager().install())




