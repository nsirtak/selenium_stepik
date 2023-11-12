#1.Открыть страницу http://suninjuly.github.io/wait1.html
#2.Нажать на кнопку "Verify"
#3.Проверить, что появилась надпись "Verification was successful!"
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
try:
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/wait1.html")
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")
    assert "successful" in message.text
finally:
    browser.quit()