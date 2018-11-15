from base.base_driver import init_driver
from page.page import Page
import pytest


class TestSearch:

    def setup(self):
        # self.driver = init_driver()
        self.page = Page(None)
    #
    # def teardown(self):
    #     self.driver.quit()

    @pytest.mark.parametrize("args", ["hello1", "xiaoming"])
    def test_search(self, args):
        self.page.setting.click_search()
        self.page.search.input_key_word(args)
        self.page.search.click_back()

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_search1(self):
        self.page.setting.click_search()
        self.page.search.click_back()