import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.implicitly_wait(5)
    yield browser
    browser.close()


@pytest.fixture(scope="function", autouse=True)
def get_url(browser):
    browser.get("https://www.python.org/")
    assert "Welcome to Python.org" == browser.title
    print("\nActual title == expected title\n")
