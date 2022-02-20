
import sys
import pyautogui, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = r"your/path/to/chromedriver"

def main():
    if(len(sys.argv) >= 2):
        if(sys.argv[1] == "-h" or sys.argv[1] == "--help"):
            print(f"\nUsage: {sys.argv[0]} --<mode>\
                \n\nMode:\n\t--normtest = to enter the normal typing test.\
                \n\t--advtest = to enter the advanced typing test.\
                \n\t--compete = to compete with other players.".expandtabs(4))
        else:
            global driver
            driver = webdriver.Chrome(path)
            if(sys.argv[1] == "--normtest"): typingTest()
            elif(sys.argv[1] == "--advtest"): advTypingTest()
            elif(sys.argv[1] == "--compete"): multiplayerTypingTest()
            else: sys.exit(1)

    else:
        print(f"\nUsage: {sys.argv[0]} --<mode>\
            \nFor more, check help section:\
            \n\t{sys.argv[0]} --help 'or' -h".expandtabs(4))


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

    typerInput.send_keys('10ff_bot')
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
    

if __name__ == "__main__":
    main()

