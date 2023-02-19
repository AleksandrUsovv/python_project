import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

driver.get('http://www.github.com')

email = driver.find_element('id', 'user_email')
email.send_keys('hello@rxample.com')
email.send_keys(Keys.ENTER)
def wait_till_clicable(driver, selector_type, selector_value):
    try:
        element = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="email-container"]/div[2]/button'))
        )
        element.click()
    except:
        print('ERROR')
        driver.quit()

cont = driver.find_element('xpath', '//*[@id="email-container"]/div[2]/button')
# time.sleep(10)

# cont.click()

print(email)