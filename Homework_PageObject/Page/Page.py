
from innopolis.Homework_PageObject.Driver import Driver
from innopolis.Homework_PageObject.Locator.Locator import YandexLocator
from innopolis.Homework_PageObject.URL import URL


class YandexPage:
    """Class discribes component on the page."""
    driver=Driver.Driver.chrome_driver

    def yandex_search(self):
        """Discription if INPPUT element."""
        yandex_search= self.driver.find_element(*YandexLocator.YANDEX_SEARCH)
        return yandex_search

    def open_yandex_page(self):
        """Open Yandex page function."""
        self.driver.get(URL.URL.YANDEX)

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




