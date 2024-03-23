import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

PROMISED_DOWNLOAD = 50
PROMISED_UPLOAD = 15
X_EMAIL = "weronika.bulenda@interia.pl"
X_PASSWORD = "W3ronika"
TWITTER = "https://twitter.com/?lang=en"
SPEEDTEST = "https://www.speedtest.net/"
SLEEP = lambda x: sleep(x)


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_settings = webdriver.ChromeOptions()
        chrome_settings.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(chrome_settings)

    def speedtest_results(self):
        self.driver.get(SPEEDTEST)
        SLEEP(4)
        self.driver.find_element(By.ID, value="onetrust-accept-btn-handler").click()
        self.driver.find_element(By.CLASS_NAME, value="start-text").click()
        SLEEP(65)
        try:
            self.driver.find_element(By.XPATH,
                                     value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div['
                                           '8]/div'
                                           '/div/p[2]/button').click()
        except selenium.common.exceptions.NoSuchElementException:
            pass
        download = self.driver.find_elements(By.CSS_SELECTOR, value=".u-align-left span")
        return download

    def x_post(self, up, down):
        self.driver.get(TWITTER)
        SLEEP(4)
        self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]/div').click()
        self.driver.find_element(By.LINK_TEXT, value="Sign in").click()
        SLEEP(4)
        mail = self.driver.find_element(By.NAME, value="text")
        mail.send_keys(X_EMAIL)
        mail.send_keys(Keys.ENTER)
        SLEEP(4)
        password = self.driver.find_element(By.NAME, value="password")
        password.send_keys(X_PASSWORD)
        password.send_keys(Keys.ENTER)
        SLEEP(7)
        self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/'
                                                 'div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/'
                                                 'div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/'
                                                 'div/div/div/div').send_keys(f"Hey Orange, why is my net speed is "
                                                                              f"{down}down/{up}up, when I pay for"
                                                                              f" {PROMISED_DOWNLOAD}down/"
                                                                              f"{PROMISED_UPLOAD}up")

        self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/'
                                                 'div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/'
                                                 'div[3]').click()
