#Задание: поиск элемента по тексту в ссылке
#https://stepik.org/lesson/138920/step/5?unit=196194

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

# переходим на нужную страницу
link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()
browser.get(link)

# высчитываем номер ссылки, находим элемент по тексту ссылки
needed_link = browser.find_element(By.PARTIAL_LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))

# нажимаем на ссылку
needed_link.click()

try:

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
