from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
driver = webdriver.Firefox(executable_path='/home/quanabi/Desktop/abi/geckodriver')
#driver.get("http://www.bzzii.glitch.me/")
driver.get('https://profitcentr.com/')
#bq = driver.page_source
'''
heliiooo0202@gmail.com
swml6c5d
git pass
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
soup = BeautifulSoup(bq, 'html.parser')
bq2 = soup.find_all('div',{'class': 'lRu31'})
print(bq2)
'''
#/html/body/div[6]/table[2]/tbody/tr/td[1]/div/a[2]
aBi =  driver.find_element(By.XPATH, "/html/body/div[6]/table[2]/tbody/tr/td[1]/div/a[2]")
aBi.click()
#driver.close()