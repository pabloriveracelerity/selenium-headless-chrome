from selenium import webdriver


def linkedin_demo():
    # pass the headless flag to chrome
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    chrome = webdriver.Chrome(chrome_options=options)

    chrome.get('https://linkedin.com')
    chrome.implicitly_wait(5)

    chrome.get_screenshot_as_file('linkedin.png')
    chrome.quit()


if __name__ == '__main__':
    print('Running demo...')
    linkedin_demo()
    print('...Done')