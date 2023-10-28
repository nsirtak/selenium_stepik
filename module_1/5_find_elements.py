#https://stepik.org/lesson/138920/step/7?unit=196194
#Задание: использование метода find_elements
from selenium.webdriver.common.by import By
from time import sleep
import time

from selenium import webdriver
try:
    # переходим на нужную страницу
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")

    #  ищем элементы через find_elements_by
    elements = browser.find_elements(By.TAG_NAME,"input")
    for element in elements:
        element.send_keys("Мой ответ")

    # нажимаем на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла