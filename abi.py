from selenium import webdriver



from selenium.webdriver.common.keys import Keys



from selenium.webdriver.common.by import By 

import requests 

import time ,re

class aBi():

  def __init__(self,name):

    self.driver = webdriver.Chrome()

    self.username = 'quanabi'

    self.password = '79zur9yw'

    self.name = name

    self.iw = 1

  def click_inp(self):

    try:

      #driver.execute_script("document.body.

      ifram2 = self.driver.find_element(By.XPATH,'/html/frameset/frame[1]')

      self.driver.switch_to.frame(ifram2)

      self.iee()

      self.driver.switch_to.default_content()

      time.sleep(2)

      self.driver.close()

      self.driver.switch_to.window(self.driver.window_handles[0])

      time.sleep(2)

    except:

      time.sleep(2)

      self.click_inp()

  def iee(self):

    if self.iw == 5:

      return 

    try:

      while True :

        abii2 = self.driver.page_source

        if 'class="timer" id="timer_inp"' in abii2 :

          abi2i = re.findall('class="timer" id="timer_inp">(.*?)<',abii2)

          

          if len(abi2i) > 0:

            print(abi2i[0])

            time.sleep(int(abi2i[0]))

            #<style>#serf-link-8164759{display:none;}</style>

          time.sleep(2)

        if '<input name="code" type="range"' in abi2i:

          self.driver.execute_script('''inp = document.getElementsByTagName("input");                                 inp[0].value = inp[0].max;''')

  

          time.sleep(1)

          self.driver.find_element(By.TAG_NAME,"button").click()

          break

            #print (self.driver.page_source)

    except:

      self.iw += 1

      time.sleep(2)

      self.iee()



  def function_cap(self,bq):

    try:

      icapa = True

      self.sendPhoto(self.name + ',' + bq)

      while icapa:

        a2 = requests.get('https://api.telegram.org/bot6691394722:AAEz0yMN644dj3Qp4GAsmKSuqmy0UWwNidQ/getUpdates').json()

        res = len(a2['result'])

        bi = a2['result'][res- 1]['message']['text']

        rei = re.findall('(.*?),',bi)

#        print(rei)

        if len(rei) > 0:

          if str(rei[0]) == str(self.name):

            if str(rei[1]) == bq:

              self.driver.find_element(By.XPATH,'//*[@id="login-form"]/table/tbody/tr[3]/td/div/label['+rei[2]+']').click()

              time.sleep(2) 

              abi1 = self.driver.find_element(By.XPATH,'//*[@id="login-form"]/button/span').click()

              time.sleep(2) 

              icapa = False

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



  def main_start(self):

    self.driver.get('https://profitcentr.com/') 

    time.sleep(2) 

    aBi = self.driver.find_element(By.XPATH, '//*[@id="leftcolumn"]/a[2]') 

    aBi.click() #login 

    time.sleep(2)

    

    abi = self.driver.find_element(By.XPATH,'//*[@id="login-form"]/table/tbody/tr[3]/td')

    abi.screenshot('aBi.png')

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

    time.sleep(20) 

    abi1 = self.driver.find_element(By.XPATH,'//*[@id="mnu_title1"]').click() 

    time.sleep(2)

    while True:

      ab2i = self.driver.find_element(By.XPATH,'//*[@id="mnu_tblock1"]/a[2]').click() 

      time.sleep(2) 

      abi = self.driver.page_source

      bq = abi

      abi = re.findall('table id="jump-link-(.*?)"',bq)

      nodisplay = re.findall('<style>#jump-link-(.*?){display:none;}</style>',bq)



      if len(nodisplay) != 0:



          for i in range(len(nodisplay)):

            for ibi in range(len(abi)):

              if nodisplay[i] == abi[ibi]:

                del abi[ibi]

      print (abi)

      if len(abi) != 0:

        for i in range(len(abi)):

          abi2 = self.driver.find_element(By.XPATH,'//*[@id="start-jump-' + str(abi[i]) + '"]/a').click()

          time.sleep(2)

          self.driver.switch_to.window(self.driver.window_handles[1])

          time.sleep(2)

          while True:

            

            self.driver.switch_to.window(self.driver.window_handles[0])

            time.sleep(1) 

            title = self.driver.title

            if 'сек..' in title :

              self.driver.switch_to.window(self.driver.window_handles[1])

              time.sleep(int(re.findall('(.*?) сек..',title)[0]) * 2)

            else:

              self.driver.switch_to.window(self.driver.window_handles[1])

              time.sleep(5)

            if 'Просмотр засчитан!' in title :

              self.driver.switch_to.window(self.driver.window_handles[1])

              print ('@@')

              self.driver.close()

              self.driver.switch_to.window(self.driver.window_handles[0])

              time.sleep(2)

              break

      else:

        

        ab2i = self.driver.find_element(By.XPATH,'//*[@id="mnu_tblock1"]/a[1]').click() 

        time.sleep(2)

        abi = self.driver.page_source

        bq = abi

        abi = re.findall('table id="serf-link-(.*?)"',bq)

        nodisplay = re.findall('<style>#serf-link-(.*?){display:none;}</style>',bq)

        if len(nodisplay) != 0:

          for i in range(len(nodisplay)):

            for ibi in range(len(abi)):

              if nodisplay[i] == abi[ibi]:

                del abi[ibi]

        print(abi)

        if len(abi) != 0:

          for i in range(len(abi)):

            print(i)

            self.driver.find_element(By.XPATH,'//*[@id="start-serf-' + str(abi[i]) + '"]/a').click()

            time.sleep(2)

            abi2 = self.driver.find_element(By.XPATH,'//*[@id="start-serf-' + str(abi[i]) + '"]/a').click()

            #//*[@id="start-serf-8163904"]/a

            self.driver.switch_to.window(self.driver.window_handles[1])

            self.click_inp()

            #<span class="timer" id="timer_inp">6</span>

      time.sleep(202)         

            

          

abi = aBi('1').main_start()             


