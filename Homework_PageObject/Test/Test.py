from innopolis.Homework_PageObject.Page.Page import YandexPage
from innopolis.Homework_PageObject.URL import URL
from innopolis.Homework_PageObject.Driver import Driver
from selenium.webdriver.common.keys import Keys


class YandexTest:
    """Test for Homework Page Object Task1."""
    def python_search_result(self):
       yandex_page=YandexPage()
       yandex_page.open_yandex_page()
       search=yandex_page.yandex_search()
       search.send_keys('python')
       submit=yandex_page.yandex_submit()
       submit.click()
       assert "no such result"





