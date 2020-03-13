import pytest
from selenium import webdriver
import time
import math
import time
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_page_contains_button_add_to_basket(browser):
    browser.get(link)
    browser.find_element_by_css_selector("[id=language_selector]>.btn").click()

    #time.sleep(30)

    button = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
    assert button > 0, 'Кнопка добавления в корзину не найдена!'