from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
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
driver.get("https://www.bdodae.com/")
sleep(3)
for i in bcolumn:
    if bcolumn.index(i) < 1:
        continue
    driver.find_element_by_xpath('//*[@id="search_button"]').click()
    sleep(3)
    driver.find_element_by_xpath('//*[@id="search"]').send_keys(i)
    driver.find_element_by_xpath('//*[@id="search"]').send_keys('\ue007')
    sleep(2)
    driver.find_element_by_xpath('//*[@id="search_results"]/a[1]').click()
    sleep(1)
    try:
        cookingAvg = driver.find_element_by_xpath('//*[@id="calc_main"]/div[1]/div[4]/div[1]/input[2]').get_attribute('value')
    except NoSuchElementException:
        print("{} of your item has no Cooking Average ".format(i))
        continue

    sheet.update_cell(bcolumn.index(i) + 1, 13, cookingAvg)
    print("{} of your item has {} Cooking Average ".format(i, cookingAvg))

