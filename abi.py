from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time ,re
import requests
from bs4 import BeautifulSoup
driver = webdriver.Firefox(executable_path='/home/quanabi/Desktop/abi/geckodriver')
#driver.get("http://www.bzzii.glitch.me/")
width = 500
height = 400
driver.set_window_size(width, height)
driver.get('https://profitcentr.com/')
time.sleep(10)
aBi = driver.find_element(By.XPATH, "/html/body/div[6]/table[2]/tbody/tr/td[1]/div/a[2]")
aBi.click() #login
time.sleep(10)
username = driver.find_element(By.NAME,'username')
username.send_keys('heliiooo0202@gmail.com')
time.sleep(2)
password = driver.find_element(By.NAME,'password')
password.send_keys('swml6c5d')
abi = driver.page_source
abi = re.findall('\n(.*Отметьте.*)\n',abi)[0]  
print(abi)
ru = abi
bq = requests.get('https://translate.googleapis.com/translate_a/single?client=gtx&sl=ru&tl=vi&dt=t&q='+ru)
print (bq.text)
a = input('...')
abi = driver.find_element(By.ID,'mnu_title1')
time.sleep(10)
abi.click()
abi =  driver.find_element(By.XPATH,'/html/body/div[9]/table[2]/tbody/tr/td[1]/div/div[2]/div/center/div[1]/a[1]')
time.sleep(5)
abi.click()
driver.find_element(By.XPATH,'/html/body/div[9]/table[2]/tbody/tr/td[2]/div/div/div/div[1]/div[1]/table/tbody/tr/td[2]')#CLASS_NAME,'
'''
heliiooo0202@gmail.com
swml6c5d
git pass
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
bq = driver.page_source
abi = open('a22.txt', 'w')
abi.write(bq)
soup = BeautifulSoup(bq, 'html.parser')
bq2 = soup.find_all('div',{'class': 'lRu31'})
print(bq2)
'''
#/html/body/div[6]/table[2]/tbody/tr/td[1]/div/a[2]
#driver.close()
