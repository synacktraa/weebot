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

def typingTest():
    driver.get('https://10fastfingers.com/typing-test/english')

    allow = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection')))
    time.sleep(2)

    if allow.text == 'Allow selection':
        allow.click()

    typerInput = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,'inputfield')))
    time.sleep(1)
    typerInput.click()

    try:
        i=1
        while True:
            word = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,f'//*[@id="row1"]/span[{i}]'))).text
            typerInput.send_keys(word)
            typerInput.send_keys(Keys.SPACE)
            i+=1
    except:
        print("Completed!")
    driver.quit()

def advTypingTest():
    driver.get('https://10fastfingers.com/advanced-typing-test/')

    allow = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection')))
    time.sleep(2)

    if allow.text == 'Allow selection':
        allow.click()

    typerInput = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,'inputfield')))
    time.sleep(1)
    typerInput.click()

    try:
        i=1
        while True:
            word = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,f'//*[@id="row1"]/span[{i}]'))).text
            typerInput.send_keys(word)
            typerInput.send_keys(Keys.SPACE)
            i+=1
    except:
        print("Completed!")
    driver.quit()    

def multiplayerTypingTest():
    driver.get('https://10ff.net/login')

    typerInput = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,'username')))
    time.sleep(1)
    typerInput.click()

    typerInput.send_keys('your_name')
    typerInput.send_keys(Keys.ENTER)

    time.sleep(15)

    input_ = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'input')))
    input_.click()

    try:
        i=1
        while True:
            word = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,f'//*[@id="game"]/div[3]/div[2]/div[1]/div/span[{i}]'))).text
            input_.send_keys(word)
            input_.send_keys(Keys.SPACE)
            i+=1
    except:
        print("Done")
    time.sleep(5)
    driver.quit()
    


# multiplayerTypingTest()
# advTypingTest()
typingTest()