from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
import random
from time import sleep
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import time
chrome_options = Options()
chrome_options.add_argument("--headless")

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("marketlist").sheet1
data = sheet.get_all_records()
bcolumn = sheet.col_values(2)
pprint(bcolumn)

driver = webdriver.Chrome("C:\devtools\driver\chromedriver89")
driver.set_window_size(1020, 890)
driver.get("https://www.naeu.playblackdesert.com/en-US/Main/Index")
sleep(3)
driver.find_element_by_xpath('//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]').click()
sleep(3)
driver.implicitly_wait((random.randint(200, 400) / 100))
driver.find_element_by_xpath('//*[@id="wrap"]/div/header/div/a[2]').click()
driver.implicitly_wait((random.randint(200, 400) / 100))
driver.find_element_by_xpath('//*[@id="js-leftProfileAcitve"]/div[2]/div/a[2]').click()
driver.implicitly_wait((random.randint(200, 400) / 100))
driver.find_element_by_xpath('//*[@id="_email"]').send_keys("feelspoeman@outlook.com")
driver.implicitly_wait((random.randint(200, 400) / 100))
driver.find_element_by_xpath('//*[@id="_password"]').send_keys("Superman556!")
driver.implicitly_wait((random.randint(200, 400) / 100))
driver.find_element_by_xpath('//*[@id="btnLogin"]').click()
driver.implicitly_wait((random.randint(200, 400) / 100))
driver.get('https://na-trade.naeu.playblackdesert.com/Intro/')
driver.find_element_by_xpath('//*[@id="serverSelectModal"]/div[2]/div/div[1]').click()
driver.find_element_by_xpath('//*[@id="serverSelectModal"]/div[2]/div/div[2]/ul/li[2]').click()
driver.find_element_by_xpath('//*[@id="moveRegion"]').click()
sleep(2)
for i in bcolumn:
    driver.find_element_by_xpath('//*[@id="wrapper"]/header/nav[2]/div[2]/button[1]/i').click()
    driver.find_element_by_xpath('//*[@id="frmSearch"]/fieldset/div/input').clear()
    driver.find_element_by_xpath('//*[@id="frmSearch"]/fieldset/div/input').send_keys(i)
    driver.find_element_by_xpath('//*[@id="frmSearch"]/fieldset/div/input').send_keys('\ue007')
    sleep(2)
    driver.find_element_by_xpath('//*[@id="market"]/div[1]').click()
    sleep(2)
    myitemprice = driver.find_element_by_xpath('//*[@id="market"]/div[2]/div[2]/p[2]').text
    myitemcount = driver.find_element_by_xpath('//*[@id="market"]/div[2]/div[3]').text
    sheet.update_cell(bcolumn.index(i)+1,4, myitemprice)
    sheet.update_cell(bcolumn.index(i)+1,11, myitemcount)
    sheet.update_cell(bcolumn.index(i)+1,12, 'Updated at {}'.format(time.asctime()))
    myoutput = "We have {} of your item, {}, for the price of {}".format(myitemcount, i, myitemprice)
    print(myoutput)

