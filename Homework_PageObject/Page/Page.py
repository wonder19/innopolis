from selenium import webdriver
from  webdriver_manager.chrome import ChromeDriverManager

from Locator.Locator import YandexLocator


class YandexPage:
    """Class discribes component on the page."""
    driver=webdriver.Chrome(ChromeDriverManager().install())
    YANDEX = 'https://ya.ru/'

    def yandex_search(self):
        """Discription if INPUT element."""
        yandex_search= self.driver.find_element(*YandexLocator.YANDEX_SEARCH)
        return yandex_search

    def open_yandex_page(self):
        """Open Yandex page function."""
        return self.driver.get(self.YANDEX)


    def quit_yandex_page_driver(self):
        """Close Driver after all."""
        self.driver.quit()

    def get_yandex_source(self):
        """Return Driver."""
        return self.driver.page_source

    def yandex_submit(self):
        """Discription if INPPUT element."""
        yandex_submit= self.driver.find_element(*YandexLocator.YANDEX_SUBMIT)
        return yandex_submit




