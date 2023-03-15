from twitterUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Twitter:

  def __init__(self, username, password):
    self.browserProfile = webdriver.ChromeOptions()
    self.browserProfile.add_experimental_option(
      "prefs", {"intl.accept_languages": "en,en_US"})
    self.browser = webdriver.Chrome("chromedriver.exe",
                                    chrome_options=self.browserProfile)
    self.username = username
    self.password = password

  def singIn(self):
    self.browser.get("https://twitter.com/i/flow/login")
    time.sleep(2)

    usernameInput = self.browser.find_element_by_xpath(
      "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input"
    ).clik.find_element_by_xpath(
      "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div"
    )

    usernameInput.send_keys(self.username)

    passwordInput = self.browser.find_element_by_xpath(
      "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input"
    )

    passwordInput.send_keys(self.password)

    btnSubmit = self.browser_find.element_by_xpath(
      "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div"
    )
    btnSubmit.click()
    time.sleep(2)


twitter = Twitter(username, password)

#login
twitter.singIn()
