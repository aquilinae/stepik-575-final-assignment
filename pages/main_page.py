from pages.base_page import BasePage


MAIN_PAGE_URL = 'http://selenium1py.pythonanywhere.com'


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
        self.url = MAIN_PAGE_URL
