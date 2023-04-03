from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from android import selectors as s


def test_plus(driver):
    driver.find_element(by=AppiumBy.XPATH, value=s.digit_2).click()
    driver.find_element(By.XPATH, s.plus).click()
    driver.find_element(By.XPATH, s.digit_5).click()
    assert driver.find_element(By.XPATH, s.expression).text == "2 Plus 5"
    driver.find_element(By.XPATH, s.equals).click()
    assert driver.find_element(
        By.XPATH, s.result).text[:-len(" Calculation result")] == "7"


def test_mines(driver):
    driver.find_element(by=AppiumBy.XPATH, value=s.digit_5).click()
    driver.find_element(By.XPATH, s.minus).click()
    driver.find_element(By.XPATH, s.digit_2).click()
    assert driver.find_element(By.XPATH, s.expression).text == "5 Minus 2"
    driver.find_element(By.XPATH, s.equals).click()
    assert driver.find_element(
        By.XPATH, s.result).text[:-len(" Calculation result")] == "3"


def test_division(driver):
    driver.find_element(by=AppiumBy.XPATH, value=s.digit_6).click()
    driver.find_element(By.XPATH, s.division).click()
    driver.find_element(By.XPATH, s.digit_2).click()
    assert driver.find_element(By.XPATH, s.expression).text == "6 Divided by 2"
    driver.find_element(By.XPATH, s.equals).click()
    assert driver.find_element(
        By.XPATH, s.result).text[:-len(" Calculation result")] == "3"


def test_multiplication(driver):
    driver.find_element(by=AppiumBy.XPATH, value=s.digit_6).click()
    driver.find_element(By.XPATH, s.multiplication).click()
    driver.find_element(By.XPATH, s.digit_2).click()
    assert driver.find_element(By.XPATH, s.expression).text == "6 Times 2"
    driver.find_element(By.XPATH, s.equals).click()
    assert driver.find_element(
        By.XPATH, s.result).text[:-len(" Calculation result")] == "12"
