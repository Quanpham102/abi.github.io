from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
import requests 
import time ,re
class aBi():
  def __init(self,name)__:
    self.driver = webdriver.Chrome()
    self.username = 'quanabi'
    self.password = '79zur9yw'
    self.name = name
  def function_cap(self,bq):
    try:
      icapa = True
      self.sendPhoto(self.name + ',' + bq)
      while icapa:
        a2 = requests.get('https://api.telegram.org/bot6691394722:AAEz0yMN644dj3Qp4GAsmKSuqmy0UWwNidQ/getUpdates').json()
        res = len(a2['result'])
        bi = a2['result'][res- 1]['message']['text']
        rei = re.findall('(.*?),',bi)
        print(rei)
        if str(rei[0]) == str(self.name):
          if str(rei[1]) == bq:
            self.driver.find_element(By.XPATH,'//*[@id="login-form"]/table/tbody/tr[3]/td/div/label['+rei[2]+']').click()
            time.sleep(2) 
            abi1 = self.driver.find_element(By.XPATH,'//*[@id="login-form"]/button/span').click()
            time.sleep(2) 
            return
    except:
      self.function_cap(bq)

  def sendPhoto(self,caption):
    chat_id ='5831792569'
    src = 'aBi.png'
    url = "https://api.telegram.org/bot6691394722:AAEz0yMN644dj3Qp4GAsmKSuqmy0UWwNidQ/sendPhoto"
    
    image = open(src,'rb')
    files =  {'photo' : image}
    data ={'chat_id': chat_id,'caption' : caption}
    response = requests.post(url, data = data, files= files)

  def main_start():
    self.driver.get('https://profitcentr.com/') 
    time.sleep(2) 
    aBi = self.driver.find_element(By.XPATH, '//*[@id="leftcolumn"]/a[2]') 
    aBi.click() #login 
    time.sleep(2) 
    abi = self.driver.page_source
    abi = re.findall('\n(.*Отметьте.*)\n',abi)[0]
    print(abi)
    ru = abi
    bq = requests.get('https://translate.googleapis.com/translate_a/single?client=gtx&sl=ru&tl=vi&dt=t&q='+ru).json()
    username = self.driver.find_element(By.NAME,'username') 
    username.send_keys(self.username) 
    time.sleep(2) 
    password = self.driver.find_element(By.NAME,'password') 
    password.send_keys(self.password)
    time.sleep(2) 
    self.function_cap(bq[0][0][0]) 
    time.sleep(2) 
    abi1 = self.driver.find_element(By.XPATH,'//*[@id="mnu_title1"]').click() 
    time.sleep(2) 
    ab2i = self.driver.find_element(By.XPATH,'//*[@id="mnu_tblock1"]/a[1]').click() 
    '''
    time.sleep(2) 
    abi = self.driver.page_source
    bq = abi
    abi = re.findall('table id="jump-link-(.*?)>',bq)
    '''
abi = aBi('1')    
