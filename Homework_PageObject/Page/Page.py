"""Discribtion of Page."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from Driver.Driver import Driver
from Locator.Locator import YandexLocator
from URLS.URL import URL


class YandexPage:
    """Class discribes components on the Yandex page."""
    driver = Driver.chrome_driver

    def search(self):
        """Discription if INPUT element."""
        yandex_search = self.driver.find_element(*YandexLocator.YANDEX_SEARCH)
        return yandex_search

    def open_page(self):
        """Open Yandex page function."""
        return self.driver.get(URL.YANDEX)

    def quit_page_driver(self):
        """Close Driver after all."""
        self.driver.quit()

    def get_source(self):
        """Return Driver."""
        return self.driver.page_source

    def submit(self):
        """Discription if INPPUT element."""
        yandex_submit = self.driver.find_element(*YandexLocator.YANDEX_SUBMIT)
        return yandex_submit

    def click_on_submit_multi_times(self):
        try:
            element=WebDriverWait(self.driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'search2__button')))
        finally:
            self.driver.quit()


