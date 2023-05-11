from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe" #change to webdriver path
driver = webdriver.Chrome(PATH)

driver.get("https://ucheck.utoronto.ca/")
username = driver.find_element_by_xpath('//*[@id="username"]')
password = driver.find_element_by_xpath('//*[@id="password"]')
button = driver.find_element_by_name('_eventId_proceed')

username.send_keys() # change to utorid
password.send_keys() #change to password
button.click()

time.sleep(1)

to_click = ('//*[@id="root"]/div[2]/div/div/div[2]/button',
            '//*[@id="f5d87fa4-41c1-41bf-9307-2eb2e7862a28-noFocus"]/fieldset/label[2]',
            '//*[@id="ebdd2acd-87ff-47aa-a7d2-059677987580-noFocus"]/fieldset/label[1]',
            '//*[@id="5c2a5703-ce69-40aa-bf5a-5ddd81335aa9-noFocus"]/fieldset/label[1]',
            '//*[@id="296a215c-8f44-4ca0-b2bc-6861ddabec3b-noFocus"]/fieldset/label[1]',
            '//*[@id="c2a1ba3f-0113-49a6-95cc-aeede171963a-noFocus"]/fieldset/label[1]',
            '//*[@id="801d8c6a-6523-437e-bb6d-fa4092dacab1-noFocus"]/fieldset/label[1]',
            '//*[@id="root"]/div/div/div/div[2]/main/div/div/div/div/div/button'
            )

for x_code in to_click:

    time.sleep(1)
    element = driver.find_element_by_xpath(x_code)

    element.click()

driver.quit()


