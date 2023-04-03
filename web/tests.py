import calendar
import time

from selenium.webdriver.common.by import By
from web.helpers.json_operations import create_json
from web.helpers.check_search import check_pages, check_names_descriptions
from web import selectors as s


json_file_path = "./result_json/{timestamp}.json"
search_word = "icq"


def test_tabs(browser):
    tabs = dict()

    upper_level_elements = browser.find_elements(
        By.XPATH, s.upper_level)
    assert len(upper_level_elements) > 0

    for element in upper_level_elements:
        lower_elements_text = list()
        element_text = element.text
        lower_level_elements = browser.find_elements(
            By.XPATH, s.lower_level.format(tab_name=element_text))
        assert len(lower_level_elements) > 0

        for lower_element in lower_level_elements:
            lower_elements_text.append(lower_element.get_property('text'))

        tabs[element_text] = lower_elements_text

    create_json(tabs, json_file_path.format(
        timestamp=calendar.timegm(time.gmtime())))


def test_search(browser):
    page_numbers_text = []
    urls_without_word_in_names_descriptions = list()

    browser.find_element(By.XPATH, s.pypi).click()
    assert "PyPI" in browser.title
    print("\nActual title == expected title\n")

    browser.find_element(By.XPATH, s.input_text).send_keys(search_word)
    browser.find_element(By.XPATH, s.search_btn).click()
    page_numbers = browser.find_elements(By.XPATH, s.page_numbers)
    print(f"page_numbers: {page_numbers}")

    if len(page_numbers) > 0:
        for page_number in page_numbers:
            if page_number.text[0].isdigit():
                page_numbers_text.append(page_number.text)
        page_number_max = max(list(map(int, page_numbers_text)))
        for page in range(1, page_number_max + 1):
            browser.get(f"https://pypi.org/search/?q={search_word}&page={page}")
            browser.implicitly_wait(5)
            urls_without_word_in_names_descriptions = \
                check_names_descriptions(browser, search_word, urls_without_word_in_names_descriptions, page)
    else:
        urls_without_word_in_names_descriptions = \
            check_names_descriptions(browser, search_word, urls_without_word_in_names_descriptions)


    print(urls_without_word_in_names_descriptions)
    print(f"len(urls_without_word_in_names_descriptions): {len(urls_without_word_in_names_descriptions)}")

    urls_without_word = check_pages(browser, search_word, urls_without_word_in_names_descriptions)
    assert len(urls_without_word) == 0, \
        f"The word didn't find in {len(urls_without_word)} case(es). List of urls: {urls_without_word}"
