import os
import pyautogui, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = "your/path/to/chromedriver"

driver = webdriver.Chrome(path)
driver.get("https://www.google.com")

def locator(selector, reference):
    outcome = WebDriverWait(driver, 10).until(EC.presence_of_element_located((selector, reference)))
    return outcome

def typingTest():
    driver.get('https://10fastfingers.com/typing-test/english')

    allow = locator(By.ID,'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection')
    time.sleep(2)

    if allow.text == 'Allow selection':
        allow.click()

    typerInput = locator(By.ID,'inputfield')
    time.sleep(1)
    typerInput.click()

    try:
        i=1
        timer = 60
        while timer > 0:                                                                       
            timer_str = locator(By.XPATH,'//*[@id="timer"]').text
            if(int(timer_str[2:]) == 0):
                timer = 60
            else: timer = int(timer_str[2:])+1
            word = locator(By.XPATH,f'//*[@id="row1"]/span[{i}]').text
            typerInput.send_keys(word)
            typerInput.send_keys(Keys.SPACE)
            i+=1
    except:
        time.sleep(timer-10)
    pyautogui.press('enter')
    wpm = locator(By.XPATH,'//*[@id="wpm"]/strong').text
    print("-"*30,"\n", f"{wpm[:-4]} wpm")
    driver.quit()

def advTypingTest():
    driver.get('https://10fastfingers.com/advanced-typing-test/')

    allow = locator(By.ID,'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection')
    time.sleep(2)

    if allow.text == 'Allow selection':
        allow.click()

    typerInput = locator(By.ID,'inputfield')
    time.sleep(1)
    typerInput.click()

    try:
        i=1
        timer = 60
        while timer > 0:                                                                       
            timer_str = locator(By.XPATH,'//*[@id="timer"]').text
            if(int(timer_str[2:]) == 0):
                timer = 60
            else: timer = int(timer_str[2:])+1
            word = locator(By.XPATH,f'//*[@id="row1"]/span[{i}]').text
            typerInput.send_keys(word)
            typerInput.send_keys(Keys.SPACE)
            i+=1
    except:
        time.sleep(timer-10)
    pyautogui.press('enter')
    wpm = locator(By.XPATH,'//*[@id="wpm"]/strong').text
    print("-"*30,"\n", f"{wpm[:-4]} wpm")
    driver.quit()  

def multiplayerTypingTest():
    driver.get('https://10ff.net/login')

    typerInput = locator(By.ID,'username')
    time.sleep(1)
    typerInput.click()

    typerInput.send_keys('your_name')
    typerInput.send_keys(Keys.ENTER)

    time.sleep(18)

    input_ = locator(By.CSS_SELECTOR,'input')
    input_.click()

    try:
        i=1
        while True:
            word = locator(By.XPATH,f'//*[@id="game"]/div[3]/div[2]/div[1]/div/span[{i}]').text
            input_.send_keys(word)
            input_.send_keys(Keys.SPACE)
            i+=1
    except:
        wpm = locator(By.XPATH, '//*[@id="game"]/div[3]/div[2]/div/div/table/tbody/tr/td[2]').text
        print("-"*30, "\n", f"{wpm}")
    time.sleep(2)
    driver.quit()
    


typingTest()
# advTypingTest()
# multiplayerTypingTest()