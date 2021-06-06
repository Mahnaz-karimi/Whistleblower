from selenium import webdriver
from time import sleep


def test_installed_on_production():
    sleep(2)  # to make sure it is loaded
    driver = webdriver.Firefox()
    driver.get("https://www.reporteasily.com")
    elem = driver.title
    assert (elem == 'Whistleblower')
    driver.close()
