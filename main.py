from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

facebook_email = 'Your Email id'
fb_password = 'Your Password'

chrome_driver_path = ""
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://tinder.com/")  # go to the tinder website


# click on login
log_in = driver.find_element(by=By.LINK_TEXT, value='Log in')
log_in.click()
time.sleep(2)

# click on more option to find-out login with facebook
driver.find_element_by_xpath(
    '//*[@id="c1006085331"]/main/div/div[1]/div/div/div[3]/span/button').click()  # more options
time.sleep(2)


# Login using facebook
login_using_facebook = driver.find_element(by=By.XPATH,
                                           value='//*[@id="c1006085331"]/main/div/div[1]'
                                                 '/div/div/div[3]/span/div[2]/button/span[2]')
login_using_facebook.click()
time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

time.sleep(2)
# email = driver.find_element_by_xpath('//*[@id="email"]').click()
# email.send_keys(facebook_email)

email = driver.find_element_by_id("email")
email.send_keys(facebook_email)
time.sleep(2)
password = driver.find_element_by_id('pass')


password.send_keys(fb_password)
password.send_keys(Keys.ENTER)
driver.switch_to.window(base_window)
print(driver.title)
time.sleep(5)

# Allow cookies
cookies = driver.find_element(by=By.XPATH,
                              value='//*[@id="c-1560500889"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
cookies.click()
time.sleep(2)


# Allow Location
allow_loc = driver.find_element(by=By.XPATH, value='//*[@id="c1006085331"]/main/div/div/div/div[3]/button[1]/span')
# find_element_by_xpath('//*[@id="c1006085331"]/main/div/div/div/div[3]/button[1]/span')
allow_loc.click()
time.sleep(2)


# Dismiss all the notifications
no_notification = driver.find_element(by=By.XPATH,
                                      value='//*[@id="c1006085331"]/main/div/div/div/div[3]/button[2]/span')
# find_element_by_xpath('//*[@id="c1006085331"]/main/div/div/div/div[3]/button[2]/span')
no_notification.click()
time.sleep(2)

# Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    # Add a 1-second delay between likes.
    time.sleep(1)

    try:
        print("called")
        like_button = driver.find_element_by_xpath(
            '//*[@id="c-1560500889"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button/'
            'span/span/span')
        like_button.click()

    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

driver.quit()
