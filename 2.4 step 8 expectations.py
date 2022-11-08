from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
def calculate(x):
    return str(math.log(abs(12*math.sin(int(x)))))


url = 'http://suninjuly.github.io/explicit_wait2.html'
driver = webdriver.Chrome()
driver.get(url)

price = WebDriverWait(driver, 13).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

btn = driver.find_element(By.ID, 'book')
btn.click()

value = driver.find_element(By.ID, 'input_value')
x = value.text
y = calculate(x)

field = driver.find_element(By.ID, 'answer')
field.send_keys(y)

submit = driver.find_element(By.ID, 'solve')
submit.click()
