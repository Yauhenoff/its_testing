from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def check_names_descriptions(browser, search_word, urls_without_word_in_names_descriptions, page=""):
    names = browser.find_elements(By.XPATH, "//*[@aria-label='Search results']//*[@class='package-snippet__name']")
    search_word_lower = search_word.lower()

    for name in names:
        if search_word_lower not in name.text.lower():
            description = browser.find_elements(By.XPATH,
                                                f"//*[@aria-label='Search results']//*[@class='package-snippet__name' and text()='{name.text}']/../../*[@class='package-snippet__description']")

            assert len(description) == 1
            if search_word_lower not in description[0].text.lower():
                print(
                    f"name without word: {name.text}, description: {description[0].text}, page: {page}")
                urls_without_word_in_names_descriptions.append(
                    browser.find_element(
                        By.XPATH,
                        f"//*[@aria-label='Search results']//*[@class='package-snippet__name' and text()='{name.text}']/../..").get_attribute(
                        'href'))
    return urls_without_word_in_names_descriptions


def check_pages(browser, search_word, urls_without_word_in_names_descriptions):
    urls_without_word = list()
    search_word_lower = search_word.lower()

    for url in urls_without_word_in_names_descriptions:
        browser.get(url)
        try:
            browser.find_element(By.XPATH, f"//*[contains(text(),'{search_word}')]")
        except NoSuchElementException:
            try:
                browser.find_element(By.XPATH, f"//*[contains(text(),'{search_word_lower}')]")
            except NoSuchElementException:
                try:
                    browser.find_element(By.XPATH, f"//*[contains(text(),'{search_word_lower[0].upper() + search_word[1:]}')]")
                except NoSuchElementException:
                    try:
                        browser.find_element(By.XPATH, f"//*[contains(text(),'{search_word.upper()}')]")
                    except NoSuchElementException:
                        urls_without_word.append(url)
    return urls_without_word
