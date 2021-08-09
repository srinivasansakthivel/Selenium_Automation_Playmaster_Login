import pytest


def pytest_configure():
    pytest.my_symbol = MySymbol()