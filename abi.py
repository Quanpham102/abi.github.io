from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By 

import requests , random

import time ,re,os,string, secrets 



class aBi():



  def __init__(self,name):

    

    options = webdriver.ChromeOptions()

        #options.add_argument("--headless")#ẩn chrome 

       # options.add_argument("--proxy-server="+self.Proxy)

    #options.add_argument("--window-size=300,425")

    options.add_argument("--disable-web-security")

    options.add_argument("--disable-site-isolation-trials")

    options.add_argument("--disable-application-cache")

    options.add_argument('--disable-blink-features=AutomationControlled')

    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    self.driver = webdriver.Chrome(options=options)

    #self.driver.get('chrome://settings/')

    #self.driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.25);')

    self.username = 'quanabi'

    self.password = '79zur9yw'

    self.name = name

    self.iw = 1

    self.src = ''

    self.idsrc = 1



  def click_element(self,element,nameli):

    try:

      self.driver.find_element(element, nameli).click() 

    except:

      print ('click_element')

      time.sleep(10)

      self.click_element(element, nameli) 



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

        if '<input name="code" type="range"' in abii2:

          print('aBi')

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

      self.sendPhoto(self.name + ',' + bq + self.idsrc  + ',')

      while icapa:

        a2 = requests.get('https://api.telegram.org/bot6691394722:AAEz0yMN644dj3Qp4GAsmKSuqmy0UWwNidQ/getUpdates').json()

        res = len(a2['result'])

        bi = a2['result'][res- 1]['message']['text']

        rei = re.findall('(.*?),',bi)#        print(rei)

        if len(rei) > 0:

          if str(rei[0]) == str(self.name):

            if str(rei[1]) == bq + self.idsrc:

              aBi02 = re.findall('(.*?)\\.',rei[2])

              if len(aBi02) > 0:

                for i in range(aBi02):

                  self.driver.find_element(By.XPATH,'//*[@id="login-form"]/table/tbody/tr[3]/td/div/label['+aBi02[i]+']').click()

              else:

                self.driver.find_element(By.XPATH,'//*[@id="login-form"]/table/tbody/tr[3]/td/div/label['+rei[2]+']').click()

              time.sleep(2) 

              abi1 = self.driver.find_element(By.XPATH,'//*[@id="login-form"]/button/span').click()

              os.remove(self.src)

              time.sleep(20) 

              if self.driver.title == 'ProfiTCentR - Вход в аккаунт на Profitcentr' :

                time.sleep(5) 

                self.login()

              icapa = False

              break

    except:

      self.function_cap(bq)



  def sendPhoto(self,caption):

    chat_id ='5831792569'

    src = self.src

    url = "https://api.telegram.org/bot6691394722:AAEz0yMN644dj3Qp4GAsmKSuqmy0UWwNidQ/sendPhoto"

    image = open(src,'rb')

    files =  {'photo' : image}

    data ={'chat_id': chat_id,'caption' : caption}

    response = requests.post(url, data = data, files= files)

    

  def login(self):

    pwd = random.randint(0,2002)

    pwd = str(pwd) + secrets.choice(string.ascii_uppercase)

    self.idsrc = pwd

    self.src = 'aBi'+ self.idsrc +'.png'

    abi = self.driver.find_element(By.XPATH,'//*[@id="login-form"]/table/tbody/tr[3]/td')

    abi.screenshot(self.src)



    abi = self.driver.page_source

    abi = re.findall('\n(.*Отметьте.*)\n',abi)[0]

    ru = abi

    bq = requests.get('https://translate.googleapis.com/translate_a/single?client=gtx&sl=ru&tl=vi&dt=t&q='+ru).json()

    username = self.driver.find_element(By.NAME,'username') 

    username.clear()

    username.send_keys(self.username) 

    time.sleep(20) 

    password = self.driver.find_element(By.NAME,'password') 

    password.clear()

    password.send_keys(self.password)

    time.sleep(1)

    self.function_cap(bq[0][0][0])



  def function_capyou(self,bq):

    try:

      icapa = True

      self.sendPhoto(self.name + ',' + bq + self.idsrc  + ',')

      while icapa:

        a2 = requests.get('https://api.telegram.org/bot6691394722:AAEz0yMN644dj3Qp4GAsmKSuqmy0UWwNidQ/getUpdates').json()

        res = len(a2['result'])

        bi = a2['result'][res- 1]['message']['text']

        rei = re.findall('(.*?),',bi)#        print(rei)

        if len(rei) > 0:

          if str(rei[0]) == str(self.name):

            if str(rei[1]) == bq + self.idsrc:

              aBi02 = re.findall('(.*?)\\.',rei[2])

              if len(aBi02) > 0:

                for i in range(aBi02):

                  self.driver.find_element(By.XPATH,'//*[@id="maincolumn"]/div/div/div[2]/form/div[1]/label['+aBi02[i]+']').click()

              else:

                self.driver.find_element(By.XPATH,'//*[@id="maincolumn"]/div/div/div[2]/form/div[1]/label['+rei[2]+']').click()

              time.sleep(2) 

              abi1 = self.driver.find_element(By.XPATH,'//*[@id="maincolumn"]/div/div/div[2]/form/button').click()

              os.remove(self.src)

              time.sleep(20) 

              if self.driver.title == 'ProfiTCentR - Вход в аккаунт на Profitcentr' :

                time.sleep(5) 

                self.login()

              icapa = False

              break

    except:

      self.function_cap(bq)



  def click_youtube(self):

    self.click_element(By.XPATH,'//*[@id="mnu_tblock1"]/a[6]')

    time.sleep(20)

    pwd = random.randint(0,2002)

    pwd = str(pwd) + secrets.choice(string.ascii_uppercase)

    self.idsrc = pwd

    self.src = 'aBi'+ self.idsrc +'.png'

    abi = self.driver.find_element(By.XPATH,'//*[@id="maincolumn"]/div/div/div[2]/form')

    abi.screenshot(self.src)

    abi = self.driver.page_source

    abi = re.findall('\n(.*Отметьте.*)\n',abi)[0]

    ru = abi

    bq = requests.get('https://translate.googleapis.com/translate_a/single?client=gtx&sl=ru&tl=vi&dt=t&q='+ru).json()

    self.function_capyou(bq[0][0][0])

    abi = self.driver.page_source

    bq = abi

    abi = re.findall('table id="ads-link-(.*?)"',bq)

    if abi > 0 :

      for i in range(abi):

        self.click_element(By.XPATH,'//*[@id="start-ads-'+ abi[i] +'"]/span[1]')

        time.sleep(20)

        abi = self.driver.page_source

        if '<span class="youtube-error">' in abi :

          pass

        else:

          bq = abi

          lik = re.findall('id="check-task-(.*?)"',bq)[0]

          sview = re.findall('data-timer="(.*?)"',bq)[0]

          self.click_element(By.XPATH,'//*[@id="check-task-'+lik+'"]')

          time.sleep(20)

          self.driver.switch_to.window(self.driver.window_handles[1])

          fram2 = driver.find_element(By.XPATH,'//*[@id="video-start"]')

          driver.switch_to.frame(fram2)

          time.sleep(20)

          fram2 = driver.find_element(By.XPATH,'//*[@id="player"]').click()

          time.sleep(20)

          self.driver.switch_to.default_content()

          time.sleep(sview)

          while True:

            src = self.driver.page_source

            if Подтвердить просмотр in src:

              self.click_element(By.XPATH,'//*[@id="succes-error"]/table/tbody/tr/td[2]/button')

              self.driver.close()

              self.driver.switch_to.window(self.driver.window_handles[0])

              time.sleep(2)

              break



  def main_start(self):

    self.driver.get('https://profitcentr.com/')

    time.sleep(2) 

    aBi = self.driver.find_element(By.XPATH, '//*[@id="leftcolumn"]/a[2]') 

    aBi.click() #login ProfiTCentR - Вход в аккаунт на Profitcentr

    time.sleep(20) 

    print(self.driver.title)

    self.login()

    self.driver.switch_to.new_window('tab')

    self.driver.get('chrome://settings/') 

    self.driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.5);')

    self.driver.set_window_size(270, 768)

    self.driver.close()

    self.driver.switch_to.window(self.driver.window_handles[0])

    time.sleep(20) 

    abi1 = self.driver.find_element(By.XPATH,'//*[@id="mnu_title1"]').click() 

    time.sleep(20)

    while True:

      #ab2i

      self.click_youtube()

      i = 2002

      if i = 2:

        pass

      else:

        ab2i = self.click_element(By.XPATH,'//*[@id="mnu_tblock1"]/a[1]')

        time.sleep(20)

        abi = self.driver.page_source

        bq = abi

        abi = re.findall('table id="serf-link-(.*?)"',bq)

        nodisplay = re.findall('<style>#serf-link-(.*?){display:none;}</style>',bq)

        abi2q = abi

        if len(nodisplay) != 0:

          if len(abi) == len(nodisplay):

            for ibi in range(len(nodisplay)):

              del abi[ibi]

          else :   

            for i in range(len(nodisplay)):

              for ibi in range(len(abi) - len(nodisplay)):

                if nodisplay[i] == abi[ibi]:

                  del abi[ibi]

            for i in range(len(nodisplay)):

                if nodisplay[i] == abi[len(abi) - i -1]:

                  del abi[len(abi) - i-1]

        if len(abi) != 0:

          print(abi)

          for i in range(len(abi)):

            print(i)

            self.click_element(By.XPATH,'//*[@id="start-serf-' + str(abi[i]) + '"]/a')

            time.sleep(10)

            abi2 = self.click_element(By.XPATH,'//*[@id="start-serf-' + str(abi[i]) + '"]/a')

            #//*[@id="start-serf-8163904"]/a

            time.sleep(5)

            self.driver.switch_to.window(self.driver.window_handles[1])

            self.click_inp()

            #<span class="timer" id="timer_inp">6</span>

      time.sleep(1800)

abi = aBi('1').main_start()
