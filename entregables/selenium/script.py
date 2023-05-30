from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://localhost:3000")

value_to_be_found = ['Integrante1', 'Integrante2', 'Integrante3', 'Integrante4', 'Integrante5', 'Integrante6']

text_box1 = driver.find_element(by=By.NAME, value="member1")
text_box2 = driver.find_element(by=By.NAME, value="member2")
text_box3 = driver.find_element(by=By.NAME, value="member3")
text_box4 = driver.find_element(by=By.NAME, value="member4")
text_box5 = driver.find_element(by=By.NAME, value="member5")
text_box6 = driver.find_element(by=By.NAME, value="member6")


text_box1.send_keys(value_to_be_found[0])
text_box2.send_keys(value_to_be_found[1])
text_box3.send_keys(value_to_be_found[2])
text_box4.send_keys(value_to_be_found[3])
text_box5.send_keys(value_to_be_found[4])
text_box6.send_keys(value_to_be_found[5])

submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

submit_button.click()


wait = WebDriverWait(driver,10)

message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".App > div > div:last-child")))

value = message.text

assert value == f'{value_to_be_found[0]} {value_to_be_found[1]} {value_to_be_found[2]} {value_to_be_found[3]} {value_to_be_found[4]} {value_to_be_found[5]}'

driver.save_screenshot("screenshot.png")

driver.quit()
