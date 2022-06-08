from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# Open DigiKala
driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.digikala.com/")
assert "دیجی‌کالا" in driver.title

# Click on login
login_element = driver.find_element_by_partial_link_text('ورود به حساب کاربری')
login_element.click()

# Enter username and click
email_phone_element = driver.find_element_by_name('login[email_phone]')
email_phone_element.clear()
email_phone_element.send_keys('najafi.nazanin@gmail.com')

login_button = None
for button in driver.find_elements_by_tag_name('button'):
    if button.text == 'ورود به دیجی‌کالا':
        login_button = button
login_button.click()

# Enter password and click
password_element = driver.find_element_by_name('login[password]')
password_element.clear()
password_element.send_keys('****')

next_button = None
for button in driver.find_elements_by_tag_name('button'):
    if button.text == 'ادامه':
        next_button = button
next_button.click()

# Check username on page
popup_element = driver.find_element_by_xpath('/html/body/header/div/div/div[2]/div[1]/div/a')
popup_element.click()

profile_element = driver.find_element_by_class_name('c-header__profile-dropdown-user-name')
if 'نازنین نجفی' not in profile_element.text:
    print('Error in login!')
else:
    print('Test ahs been completed successfully!')

sleep(3)
driver.close()
