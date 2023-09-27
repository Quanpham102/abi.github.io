from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from bs4 import BeautifulSoup
driver = webdriver.Firefox(executable_path='/home/quanabi/Desktop/abi/geckodriver')
#driver.get("http://www.bzzii.glitch.me/")
driver.get('https://profitcentr.com/')
time.sleep(10)
aBi = driver.find_element(By.XPATH, "/html/body/div[6]/table[2]/tbody/tr/td[1]/div/a[2]")
aBi.click() #login
time.sleep(10)
username = driver.find_element(By.NAME,'username')
username.send_keys('heliiooo0202@gmail.com')
time.sleep(10)
password = driver.find_element(By.NAME,'password')
password.send_keys('swml6c5d')
input('...')
abi = driver.find_element(By.ID,'mnu_title1')
abi.click()
abi =  driver.find_element(By.XPATH,'/html/body/div[9]/table[2]/tbody/tr/td[1]/div/div[2]/div/center/div[1]/a[1]')

click
driver.find_element(By.XPATH,'/html/body/div[9]/table[2]/tbody/tr/td[2]/div/div/div/div[1]/div[1]/table/tbody/tr/td[2]')#CLASS_NAME,'
'''
heliiooo0202@gmail.com
swml6c5d
git pass
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
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
