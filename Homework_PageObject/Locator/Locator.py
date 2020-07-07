from selenium.webdriver.common.by import By

class YandexLocator:
    YANDEX_SEARCH=(By.NAME, 'text')
    YANDEX_SUBMIT=(By.CLASS_NAME, 'search2__button')


class Python:
    PYTHON_DOWNLOADS=(By.LINK_TEXT,'https://www.python.org/ftp/python/3.8.3/Python-3.8.3.tar.xz')