from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

username_input = driver.find_element_by_css_selector("input#user-name.input_error.form_input")
password_input = driver.find_element_by_css_selector("input#password.input_error.form_input")
username_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")
password_input.send_keys(Keys.RETURN)

add_buttons = driver.find_elements_by_css_selector("button.btn_inventory")
for button in add_buttons:
    button.click()

cart_button = driver.find_element_by_css_selector("a.shopping_cart_link")
cart_button.click()

checkout_button = driver.find_element_by_css_selector("button#checkout")
checkout_button.click()

continue_button = driver.find_element_by_css_selector("input#continue")
continue_button.click()

total_price = driver.find_element_by_css_selector("div.summary_total_label")
driver.save_screenshot("total_price.png")

finish_button = driver.find_element_by_css_selector("button#finish")
finish_button.click()

backhome_button = driver.find_element_by_css_selector("button#back-to-products")
backhome_button.click()

logout_button = driver.find_element_by_css_selector("a#logout_sidebar_link")
logout_button.click()

driver.quit()