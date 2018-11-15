import time
import pytest


class TestContact:

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test_hello1(self):
        print("hello1")
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test_hello2(self):
        print("hello1")
        assert 0


