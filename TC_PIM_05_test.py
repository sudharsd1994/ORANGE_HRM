import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from config import TestData
from locators import Locators

driver = webdriver.Chrome()

class TestCases:

    def test_login_page_title(self):
        driver.get(TestData.BASE_URL)
        driver.implicitly_wait(10)
        driver.maximize_window()
        title = driver.title
        print(title)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_do_login(self):
        driver.find_element(By.XPATH,Locators.USER_NAME).send_keys(TestData.USER_NAME)
        driver.find_element(By.XPATH,Locators.PASSWORD).send_keys(TestData.PASSWORD)
        driver.find_element(By.XPATH,Locators.LOGIN_BUTTON).click()
        driver.implicitly_wait(10)

    def test_d0_click(self):
        driver.find_element(By.XPATH,Locators.PIM_MODULE).click()
        driver.find_element(By.XPATH,Locators.PIM_DELETE).click()

    def test_do_conform_delete(self):
        driver.find_element(By.XPATH,Locators.PIM_CONFIRM_DELETE).click()
        driver.implicitly_wait(10)
        driver.close()
