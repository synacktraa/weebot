
import argparse
from argparse import RawTextHelpFormatter
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = r"C:\Users\harsh\chromedriver_win32\chromedriver.exe"

def main():
    parser = argparse.ArgumentParser(description="A super fast typer bot for 10fastfingers.com", formatter_class=RawTextHelpFormatter)
    parser.add_argument('-l', '--login', metavar='', help='plays with user specified profile.\nFormat= --login <email-id>&passwd')
    parser.add_argument('-t', '--tempo', metavar='', help='plays with user specified speed.\nFormat= --tempo <int>x\n\t  --tempo max')
    mode = parser.add_argument_group("typing mode arguments")
    mode.add_argument('-n', '--normtest', action='store_true', help='enters the normal typing test')
    mode.add_argument('-a', '--advtest', action='store_true', help='enters the advanced typing test')
    mode.add_argument('-c', '--compete', action='store_true', help='enters the competitive mode')

    args = parser.parse_args()
    
    global driver
    driver = webdriver.Chrome(path)
    
    if (bool(args.login)):

        loginArr = args.login.split('>&')
        login_(loginArr[0][1:], loginArr[1])
        loggedIn = True
    else:

        loggedIn = False
        driver.get("https://10fastfingers.com")
        allow = locator(By.ID,'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection')
        time.sleep(2)

        if allow.text == 'Allow selection':
            allow.click()

    if(bool(args.tempo)):
        speed = args.tempo
    else:
        speed = "1x"

    argument = arg_validator(args.normtest, args.advtest, args.compete)
    if argument == '-n' or argument == '-a':
        typeIt(argument, speed, loggedIn)
    elif argument == '-c':
        multiplayerTypingTest()
    elif argument == -1:
        parser.error("atleast select one mode.")  
    else:
        parser.error("select only one mode.")  
    # print(login.split('>&')[0][1:])

def arg_validator(f_arg, s_arg, th_arg):
    if(f_arg and not s_arg and not th_arg):
        return "-n"
    elif(s_arg and not f_arg and not th_arg):
        return "-a"
    elif(th_arg and not s_arg and not f_arg):
        return "-c"
    elif(not th_arg and not s_arg and not f_arg):
        return -1
    else: return 0

def locator(selector, reference):
    outcome = WebDriverWait(driver, 10).until(EC.presence_of_element_located((selector, reference)))
    return outcome

def login_(email, password):

    driver.get("https://10fastfingers.com/login")
    allow = locator(By.ID,'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection')
    time.sleep(2)

    if allow.text == 'Allow selection':
        allow.click()
    
    email_box = locator(By.ID, "UserEmail")
    time.sleep(1)
    email_box.click()
    email_box.send_keys(email)

    password_box = locator(By.ID, "UserPassword")
    time.sleep(1)
    password_box.click()
    password_box.send_keys(password)
    password_box.send_keys(Keys.ENTER)


def typeIt(arg, speed, auth):

    if arg == '-n':
        if(auth):
            pass
        else:
            norSec = locator(By.XPATH, '//*[@id="sidebar"]/div/a[1]')
            time.sleep(0.5)
            norSec.click()
    elif arg == '-a':
        if(auth):
            driver.get('https://10fastfingers.com/advanced-typing-test/english')
        else:
            advSec = locator(By.XPATH, '//*[@id="sidebar"]/div/a[2]')
            time.sleep(0.5)
            advSec.click()

    typerInput = locator(By.ID,'inputfield')
    time.sleep(1)
    typerInput.click()

    nSpeed = 0.1
    i=1
    timer = 60
    try:
        while timer > 0:                                                                       
            timer_str = locator(By.XPATH,'//*[@id="timer"]').text
            if(timer_str == "1:00"):
                timer = 60
            else: 
                timer = int(timer_str[2:])
                print(timer)
            word = locator(By.XPATH,f'//*[@id="row1"]/span[{i}]').text
            for char in word:
                typerInput.send_keys(char)
                if(speed ==  "max"):
                    pass
                else:
                    time.sleep(nSpeed/int(speed[:-1]))
            typerInput.send_keys(Keys.SPACE)
            i+=1

    except:
        if timer == 0:
            wpm = locator(By.XPATH,'//*[@id="wpm"]/strong').text
            print("-"*30,"\n", f"{wpm[:-4]} wpm")
            driver.quit()
        else:
            print(timer)
            time.sleep(timer)
            alert_obj = driver.switch_to.alert
            alert_obj.dismiss()

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
        wpm = wpm.replace(" ", "").split()
        print("-"*30, "\n", f"{wpm[0]} WPM")
    time.sleep(2)
    driver.quit()
    

if __name__ == "__main__":
    main()

