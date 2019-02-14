from selenium import webdriver
import os
import requests


def test_links(links):
    for link in links:
        request = requests.get(link)
        if request.status_code != 200:
            print('Found bad URL: ' + link)
            print('Code: ' + str(request.status_code))
            return
    print('No broken URLs!')


def test_dewey():
    root_dir = os.getcwd()
    utils_dir = os.path.abspath(root_dir + "/../utils/")
    driver = webdriver.Chrome(executable_path=utils_dir + '/chromedriver')

    driver.get("https://kyledewey.github.io/")
    links_elements = driver.find_elements_by_tag_name('a')

    links = list(map(lambda e: e.get_attribute('href'), links_elements))

    test_links(links)

    driver.quit()


if __name__ == '__main__':
    test_dewey()
