upper_level = "//*[@id='mainnav']//*[contains(@class, 'tier-1')]"
lower_level = "//*[@id='mainnav']//*[text()='{tab_name}']/.." \
              "//*[contains(@class,'tier-2')]/*[@href and @title]"
pypi = "//*[text()='PyPI']"
input_text = "//*[@id='search']"
search_btn = "//button[@class='search-form__button']"
page_numbers = "//*[contains(@class, 'button-group')]//*[contains(@class, 'button')]"
