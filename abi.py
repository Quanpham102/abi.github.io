a2 = self.driver.page_source
linkview = re.findall('div class="" id="curLimit">(.*?)<',a2)
if len(linkview) > 0:
  for i in range(len(linkview)):
    self.driver.switch_to.window(self.driver.window_handles[1])
    ifram2 = self.driver.find_element(By.XPATH,'//*[@id="task_video"]')
    self.driver.switch_to.frame(ifram2) 
    time.sleep(2)
    self.driver.find_element(By.XPATH,'//*[@id="player"]').click()
    self.driver.switch_to.default_content()
    time.sleep(2)
    abii2 = self.driver.page_source
    abi2i = re.findall('div id="timer" class="timer">(.*?)<',abii2)
    time.sleep(abi2i)
    while True:
      abii2 = self.driver.page_source
      if '$0.00022' in abii2:
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
