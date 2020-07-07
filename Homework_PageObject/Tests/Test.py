from Page.Page import YandexPage


def test_yandex_search_python_result():
    ya = YandexPage()
    ya.open_yandex_page()
    search = ya.yandex_search()
    search.send_keys('python')
    submit = ya.yandex_submit()
    submit.click()
    assert "python" not in ya.get_yandex_source(), 'No such result'
    ya.quit_yandex_page_driver()


def test_submit_multi_click():
    ya = YandexPage()
    ya.open_yandex_page()
    ya.click_on_submit_multi_times()
