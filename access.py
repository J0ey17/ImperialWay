import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import telegram

def dLaunch(opt,url):

    options = Options()
    options.headless = True
    global driver
    if opt == "head":
        driver = webdriver.Firefox()
    elif opt == "headless":
        driver = webdriver.Firefox(options=options)
    driver.get(url)

def telConnect(msg):
    bot = telegram.Bot(token=<telegram bot token>)  #Input needed
    bot.sendMessage(chat_id=<telegram chatid>,text=msg) #Input needed

def impLogin(uname,upass,realm_no):

    elem = driver.find_element(By.ID, "login-user")
    elem.clear()
    elem.send_keys(uname)
    elem = driver.find_element(By.ID, "login-pass")
    elem.clear()
    elem.send_keys(upass)
    elem.send_keys(Keys.ENTER)
    time.sleep(5)
    driver.find_element(By.XPATH,"//input[@value='"+realm_no+"']").submit()
    time.sleep(10)
    try:
        driver.execute_script("javascript:void(container.close({saveName: 'modal', cancelCallback: true, flow: true, closedWith: 'click'}))")
    except:
        pass

def impLogout():
    time.sleep(3)
    driver.execute_script("javascript:void((function(){$('#ui-slidebar').stop().slideToggle();$(window).trigger('toggleSettingsContainer');}()));")
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[@title='Logout']").click()
    time.sleep(3)
    driver.quit()

def vassCollect():
    print("Under Development")

def caveAttackExt(preset):
    preset -= 1
    time.sleep(5)
    driver.execute_script("xajax_viewOperationCenter(container.open({saveName: 'operation-center', title: 'Command Center'}), {'tab':'attack','userId':5001});container.close({saveName: 'dungeon-attack'});SetFocusTop();")
    time.sleep(5)
    driver.find_element(By.ID,"preset"+str(preset)).click()
    
def caveAttack(template):
    time.sleep(5)
    caveAttackExt(template)
    time.sleep(2)
    while  driver.find_element(By.ID,"armyCapacity").text == "0":
        driver.execute_script("javascript:void(container.close({saveName: 'operation-center', cancelCallback: true, flow: true, closedWith: 'click'}))")
        time.sleep(3)
        caveAttackExt(template)
    attType = ["Field battle","Fortress Siege"]
    try:
        driver.find_element(By.XPATH,"//button[@value='"+attType[0]+"']").click()
    except:
        driver.find_element(By.XPATH,"//button[@value='"+attType[1]+"']").click()
    telConnect("Cave Attack Launched!")
