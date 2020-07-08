from Page.Page import YandexPage


def test_yandex_search_python_result():
    ya = YandexPage()
    ya.open_page()
    search = ya.search()
    search.send_keys('python')
    submit = ya.submit()
    submit.click()
    assert "!123" in ya.get_source(), 'No such result'
    ya.quit_page_driver()


def test_submit_multi_click():
    ya = YandexPage()
    ya.open_page()
    ya.click_on_submit_multi_times()

