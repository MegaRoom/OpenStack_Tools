import os
import time
import datetime
import sys
import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def TakeScreenShot(URL, FILENAME, PATH):
  ScreenShotPath = os.path.join(PATH, FILENAME)

  # Open Web Browser & Resize 720P
  driver = webdriver.Firefox()
  driver.set_window_size(1280, 720) 
  driver.get(URL)

  time.sleep(3)

  # Send Shift key
  driver.find_element_by_tag_name('body').send_keys(Keys.SHIFT)
  # Get Screen Shot
  driver.save_screenshot(ScreenShotPath)
  # Close Web Browser
  driver.quit()



if __name__=="__main__":
  #Check whether user input URL or not
  if len(sys.argv) == 2:
    argvs = sys.argv
  else:
      raise AssertionError('Give me an URL')

  if 'http' not in argvs[1]:
      raise AssertionError('Give me an URL')

  #Set Paramater
  URL = argvs[1]
  CURRENT = os.path.dirname(os.path.abspath(__file__))
  FILENAME =  re.compile("^.*token=").sub("",URL) + ".png"
  TODAY = str(datetime.date.today())
  PATH = os.path.join(CURRENT, 'screenshot')
  PATH = os.path.join(PATH, TODAY)

  #Create Directory
  if not os.path.exists(PATH):
    os.makedirs(PATH)
  TakeScreenShot(URL, FILENAME, PATH);
