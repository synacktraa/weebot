#=================================================
#       Typing Bot
#   version = "v1.0.2"
#   Author: HackitMikey (Mikey)
#
# Python3.x based typing bot for 10fastfingers.com
#===================================================

import argparse, re, time
from argparse import RawTextHelpFormatter
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = r"C:\Users\harsh\chromedriver_win32\chromedriver.exe"

def main():

    parser = argparse.ArgumentParser(description="A super fast typer bot for 10fastfingers.com", formatter_class=RawTextHelpFormatter)
    parser.add_argument('-l', '--login', metavar='', help='plays with user specified profile.\nFormat= --login <email-id>&passwd')
    parser.add_argument('-u', '--user', metavar='', help='plays with user specified name(only applicable in competitive mode).\nFormat= --user name')
    parser.add_argument('-t', '--tempo', metavar='', help='plays with user specified speed.\nFormat= --tempo <int>x\n\t  --tempo max')
    mode = parser.add_argument_group("typing mode arguments")
    mode.add_argument('-n', '--normtest', action='store_true', help='enters the normal typing test')
    mode.add_argument('-a', '--advtest', action='store_true', help='enters the advanced typing test')
    mode.add_argument('-c', '--compete', action='store_true', help='enters the competitive mode')

    args = parser.parse_args()
    
    global driver

    if(bool(args.tempo)):
        speed = args.tempo
    else:
        speed = "1x"
    
    if (bool(args.login)):
        
        Regex = re.compile(r'^<[a-zA-Z0-9._%+-]+@gmail\.com>&[a-zA-Z0-9._%+-]')
        validate = Regex.search(args.login)
        if not validate:
            parser.error("format: <user.email@gmail.com>&passwd")
        else:
            driver = webdriver.Chrome(path)
            loginArr = args.login.split('>&', 1)
            login_(loginArr[0][1:], loginArr[1])
            loggedIn = True

            # norSec = locator(By.XPATH, '//*[@id="sidebar"]/div/a[1]')
            # time.sleep(0.5)
            # norSec.click()
            # new = locator(By.XPATH, '//*[@id="main"]/div[1]')
            # time.sleep(1)

            # if(bool(new.text)):
            #     print(f"{'-'*30}\nAuthentication failed: Email or Password is wrong. Please try again.")
            #     # driver.quit()
            #     exit(0)
    else:
        # //*[@id="main"]/div[1]

        loggedIn = False
        driver = webdriver.Chrome(path)
        driver.get("https://10fastfingers.com")
        allow = locator(By.ID,'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection')
        time.sleep(2)

        if allow.text == 'Allow selection':
            allow.click()

    argument = arg_validator(args.normtest, args.advtest, args.compete)
    if argument == '-n' or argument == '-a':
        if(bool(args.user)):
            parser.error("only applicable with competitive mode.")
            driver.quit()
        else:
            typeIt(argument, speed, loggedIn)
    elif argument == '-c':
        if(bool(args.user) == 0):
            user = "10ff_bot"
        else:
            user = args.user
        multiplayerTypingTest(speed, user)
    elif argument == -1:
        argument = '-n'
        typeIt(argument, speed, loggedIn)

    else:
        parser.error("select only one mode.")  
        driver.quit()

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
    time.sleep(0.5)
    email_box.click()
    email_box.send_keys(email)

    password_box = locator(By.ID, "UserPassword")
    time.sleep(0.5)
    password_box.click()
    password_box.send_keys(password)
    password_box.send_keys(Keys.ENTER)


def typeIt(arg, speed, auth):

    try:
        main_logo = locator(By.XPATH, '//*[@id="main-logo"]')
        time.sleep(0.5)
        if(bool(main_logo) and auth):
            print(f"{'-'*40}\nAuthentication failed: Email or Password is wrong. Please try again.")
            driver.quit()
            exit(1)
    except:
        pass

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
    time.sleep(0.5)
    typerInput.click()

    nSpeed = 0.2
    i=1
    timer = 1
    try:
        while timer > 0:                                                                       
            timer_str = locator(By.XPATH,'//*[@id="timer"]').text
            if(timer_str == "1:00"):
                timer = 60
            else: 
                timer = int(timer_str[2:])
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
            time.sleep(timer-5)
            alert_obj = driver.switch_to.alert
            alert_obj.dismiss()

    wpm = locator(By.XPATH,'//*[@id="wpm"]/strong').text
    print("-"*30,"\n", f"{wpm[:-4]} wpm")
    driver.quit()
    

def multiplayerTypingTest(speed, username):
    
    driver.get('https://10ff.net/login')

    typerInput = locator(By.ID,'username')
    typerInput.click()

    typerInput.send_keys(username)
    typerInput.send_keys(Keys.ENTER)

    check = '10'
    while check != '1':
        check = locator(By.XPATH, '//*[@id="game"]/div[2]/div').text 
        i = 1
        driver.implicitly_wait(i)

    input_ = locator(By.CSS_SELECTOR,'input')
    input_.click()

    try:
        nSpeed = 0.2
        i=1
        while i:
            word = locator(By.XPATH,f'//*[@id="game"]/div[3]/div[2]/div[1]/div/span[{i}]').text
            for char in word:
                input_.send_keys(char)
                if(speed ==  "max"):
                    pass
                else:
                    time.sleep(nSpeed/int(speed[:-1]))
            input_.send_keys(Keys.SPACE)
            i+=1
    except:
        for i in range(1, 6):
            user = locator(By.XPATH, f'//*[@id="game"]/div[3]/div[2]/div/div/table/tbody/tr[{i}]/td[1]').text.replace(" ", "")
            if user != username: continue
            else: break
        wpm = locator(By.XPATH, f'//*[@id="game"]/div[3]/div[2]/div/div/table/tbody/tr[{i}]/td[2]').text
        wpm = wpm.replace(" ", "").split()
        print("-"*30, "\n", f"{wpm[0]} WPM")
    time.sleep(2)
    driver.quit()
    

if __name__ == "__main__":
    main()

