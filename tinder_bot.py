from selenium import webdriver
from time import sleep
import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TinderBot():
    #variables
    swipesPerMinute = 90
    chromeDriver = ".\chromedriver_win32\\chromedriver.exe"
    websiteLink = "https://tinder.com/"
    likeXpath = '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button'
    dislikeXpath = '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button'
    closePopup = '//*[@id="modal-manager"]/div/div/div[2]/button[2]'
    closeMatch = '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a'
    wait = ""
    
    def __init__(self):
        self.driver = webdriver.Chrome(self.chromeDriver)

    def waitForLogin(self, desiredUrl):
        self.wait.until(
            lambda driverwaiter: driverwaiter.current_url == desiredUrl)
        print("Login Successfull. Activating Auto-swipe in 20 seconds. Please Wait...")
        sleep(20)
        self.auto_swipe()

    def open_website(self):
        self.driver.get(self.websiteLink)
        self.wait = WebDriverWait(self.driver, 45) #45 seconds to login
        self.waitForLogin("https://tinder.com/app/recs")
        sleep(2)

    def like(self):
        like_btn = self.driver.find_element_by_xpath(self.likeXpath)
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath(self.dislikeXpath)
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            if(isPageLoaded()==False):
                sleep(30)
            sleep(60/self.swipesPerMinute)
            try:
                # 80 to 20 percentage
                randNumber = random.randint(0, 100)
                if(randNumber<80):                
                    self.like()
                else:
                    self.dislike()
            except Exception: #random popups handeling
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath(self.closePopup)
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath(self.closeMatch)
        match_popup.click()

    def isPageLoaded(self):
        try:
            self.driver.find_element_by_xpath(self.closeMatch)
            return True
        except Exception:
            return False
        return
        

    
bot = TinderBot()
bot.open_website()
bot.maximize_window()


'''
Credits: Written by Syed Ahsan Ahmed
Fiverr: fiverr.com/ahsanahmedsn
'''
