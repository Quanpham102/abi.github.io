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

abi = driver.page_source
abi = re.findall('\n(.*Отметьте.*)\n',abi)[0]  
print(abi)
ru = abi
bq = requests.get('https://translate.googleapis.com/translate_a/single?client=gtx&sl=ru&tl=vi&dt=t&q='+ru)
print (bq.text)
username = driver.find_element(By.NAME,'username')
username.send_keys('heliiooo0202@gmail.com')
time.sleep(2)
password = driver.find_element(By.NAME,'password')
password.send_keys('swml6c5d')
ProfiTCentR - Вход в аккаунт на Profitcentr


a = input('abi ...')
abi1 = driver.find_element(By.XPATH,'//*[@id="mnu_title1"]')
print(abi1)
driver.execute_script("arguments[0].click();",abi1)
time.sleep(2)
ab2i =  driver.find_element(By.XPATH,'/html/body/div[9]/table[2]/tbody/tr/td[1]/div/div[2]/div/center/div[1]/a[1]')
time.sleep(5)
ab2i.click()
ab2i =  driver.find_element(By.CSS_SELECTOR,'#start-serf-8144063 > a:nth-child(1)').click()
ab2i =  driver.find_element(By.CSS_SELECTOR,'.butt-yes-test')#view






ab2i =  driver.find_element(By.XPATH,'/html/body/table/tbody/tr/td[2]/table/tbody/tr/td[2]/form/button')

driver.find_element(By.XPATH,'/html/body/div[9]/table[2]/tbody/tr/td[2]/div/div/div/div[1]/div[1]/table/tbody/tr/td[2]')

#CLASS_NAME,'
'''
lass="usermnutitle-g"> is not clickable at point (102,452) because another element <html> obscures it
element = driver.find_element_by_id('lg_1166')
driver.execute_script("arguments[0].click();", element)

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
