#=================================================
#       Typing Bot
#   version = "v1.0.4"
#   Author: SynAcktraa (Mikey)
#
# Python3.x based typing bot for 10ff.net
#=================================================

import argparse, time
from argparse import RawTextHelpFormatter
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = r"C:\Users\harsh\chromedriver_win32\chromedriver.exe"

def main():

    parser = argparse.ArgumentParser(description="An efficient typing bot for 10ff.net", formatter_class=RawTextHelpFormatter)
    parser.add_argument('-u', '--user', metavar='', help='plays with user specified name\nformat = --user name')
    parser.add_argument('-t', '--tempo', metavar='', help='plays with user specified speed\nformat = --tempo [ <int>x | max ]')

    args = parser.parse_args()
    
    if(bool(args.tempo)):speed = args.tempo
    else:speed = "1x"

    if(bool(args.user) == 0): user = "bot"
    else: user = args.user

    compete(speed, user)

def locator(driver, selector, reference):
    outcome = WebDriverWait(driver, 10).until(EC.presence_of_element_located((selector, reference)))
    return outcome


def compete(speed, username):
    
    driver = webdriver.Chrome(path)
    driver.get('https://10ff.net/login')

    typerInput = locator(driver, By.ID,'username')
    typerInput.click()

    typerInput.send_keys(username)
    typerInput.send_keys(Keys.ENTER)

    check = '10'
    while check != '1':
        check = locator(driver, By.XPATH, '//*[@id="game"]/div[2]/div').text 
        driver.implicitly_wait(1)

    input_ = locator(driver, By.CSS_SELECTOR,'input')
    input_.click()

    try:
        nSpeed = 0.2
        i=1
        if speed == "max":pass
        else:time.sleep(nSpeed/int(speed[:-1]))
        while i:
            word = locator(driver, By.XPATH,f'//*[@id="game"]/div[3]/div[2]/div[1]/div/span[{i}]').text
            for char in word:
                input_.send_keys(char)
            input_.send_keys(Keys.SPACE)
            i+=1
    except:
        for i in range(1, 6):
            user = locator(driver, By.XPATH, f'//*[@id="game"]/div[3]/div[2]/div/div/table/tbody/tr[{i}]/td[1]').text.replace(" ", "")
            if user != username:continue
            else:break
        wpm = locator(driver, By.XPATH, f'//*[@id="game"]/div[3]/div[2]/div/div/table/tbody/tr[{i}]/td[2]').text.replace(" ", "").split()
        print("-"*30, "\n", f"{wpm[0]} WPM")

    time.sleep(2)
    driver.quit()
    

if __name__ == "__main__":
    main()

