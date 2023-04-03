import pytest
from appium import webdriver


@pytest.fixture(scope="session")
def driver():
    capability = {
        "platformName": "Android",
        "appPackage": "com.sec.android.app.popupcalculator",
        "appActivity": "com.sec.android.app.popupcalculator.Calculator"
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", capability)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
