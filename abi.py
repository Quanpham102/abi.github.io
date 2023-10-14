from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time ,re
import requests
width = 800
height = 400
driver = webdriver.Chrome()
driver.set_window_size(width, height)
driver.get('https://profitcentr.com/login')
#login
time.sleep(10)
username = driver.find_element(By.NAME,'username')
username.send_keys('quanabi')
time.sleep(5)
password = driver.find_element(By.NAME,'password')
password.send_keys('79zur9yw')
abi = driver.page_source
abi = re.findall('\n(.*Отметьте.*)\n',abi)[0]  
print(abi)

a = input('...')
driver.find_element(By.XPATH,'//*[@id="mnu_title1"]').click()
time.sleep(10)
driver.find_element(By.XPATH,'//*[@id="mnu_tblock1"]/a[6]').click()
abi = driver.page_source
abi = re.findall('\n(.*Отметьте.*)\n',abi)[0]
ru = abi
bq = requests.get('https://translate.googleapis.com/translate_a/single?client=gtx&sl=ru&tl=vi&dt=t&q='+ru)
print (bq.text)
abi = driver.find_element(By.XPATH,'//*[@id="maincolumn"]/div/div/div[2]/form')
abi.screenshot('bq.png')
input()
abi = driver.page_source
abi = re.findall('table id="ads-link-(.*?)"',abi)
print(abi)
driver.find_element(By.XPATH,'//*[@id="start-ads-'+abi[0]+'"]/span[1]').click()
abi2 = driver.page_source
'''
view youtube

span class="timer" id="tmr" translate="no">5831792569

ckek timer
click space play view afd
//*[@id="succes-error"]/table/tbody/tr/td[2]/button
click view xong close table
'''
