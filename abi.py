from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
driver = webdriver.Firefox(executable_path='/home/quanabi/Desktop/abi/geckodriver')
#driver.get("http://www.bzzii.glitch.me/")
driver.get('https://profitcentr.com/')
#bq = driver.page_source
'''
soup = BeautifulSoup(bq, 'html.parser')
bq2 = soup.find_all('div',{'class': 'lRu31'})
print(bq2)
'''
#/html/body/div[6]/table[2]/tbody/tr/td[1]/div/a[2]
login =  driver.find_element(By.XPATH, "/html/body/div[6]/table[2]/tbody/tr/td[1]/div/a[2]")
login.click()
driver.close()