from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

PROMISSED_DOWN = 18
PROMISSED_UP = 10


class InternetSpeedTwitterBot:
    def __init__(self):
        self.s = Service("YOUR CHROME DRIVER PATH")
        self.driver = webdriver.Chrome(service=self.s)
        self.download = 0
        self.upload = 0

    def get_internet_speed(self):
        self.driver.get("http://speedtest.net")
        sleep(5)
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()
        sleep(40)
        self.download = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span")
        self.upload = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        sleep(2)
        username = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        username.send_keys(TWITTER USERNAME)
        username.send_keys(Keys.ENTER)
        sleep(3)
        password = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]")
        password.send_keys(TWITTER PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(5)
        tweet_poster = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
        tweet = f"download speed:{self.download} and upload speed:{self.upload}"
        tweet_poster.send_keys(tweet)
        tweet_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span")
        tweet_button.click()
        sleep(2)
        self.driver.quit()

twitter_bot = InternetSpeedTwitterBot()
twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()
