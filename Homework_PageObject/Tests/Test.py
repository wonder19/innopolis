from Page.Page import YandexPage


def test_python_search_result():
    ya = YandexPage()
    ya.open_yandex_page()
    search = ya.yandex_search()
    search.send_keys('python')
    submit = ya.yandex_submit()
    submit.click()
    assert "no such result"
    ya.quit_yandex_page_driver()
