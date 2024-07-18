# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestQuizkardo():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_quizkardo(self):
    # Test name: quiz kardo
    # Step # | name | target | value
    # 1 | open | /index_1Q.html | 
    self.driver.get("http://127.0.0.1:5500/index_1Q.html")
    # 2 | setWindowSize | 1536x864 | 
    self.driver.set_window_size(1536, 864)
    # 3 | click | xpath=//label[contains(.,'git clone')] | 
    self.driver.find_element(By.XPATH, "//label[contains(.,\'git clone\')]").click()
    # 4 | click | id=submit_1 | 
    self.driver.find_element(By.ID, "submit_1").click()
    # 5 | click | xpath=//label[contains(.,'A request for code review and merging changes')] | 
    self.driver.find_element(By.XPATH, "//label[contains(.,\'A request for code review and merging changes\')]").click()
    # 6 | click | id=submit_2 | 
    self.driver.find_element(By.ID, "submit_2").click()
    # 7 | click | xpath=//label[contains(.,'package.json')] | 
    self.driver.find_element(By.XPATH, "//label[contains(.,\'package.json\')]").click()
    # 8 | click | id=submit_3 | 
    self.driver.find_element(By.ID, "submit_3").click()
    # 9 | click | xpath=//label[contains(.,'To specify files and directories that should be excluded from version control')] | 
    self.driver.find_element(By.XPATH, "//label[contains(.,\'To specify files and directories that should be excluded from version control\')]").click()
    # 10 | click | id=submit_4 | 
    self.driver.find_element(By.ID, "submit_4").click()
    # 11 | click | css=#my_row_5 .mb-10:nth-child(4) > .font-weight-normal | 
    self.driver.find_element(By.CSS_SELECTOR, "#my_row_5 .mb-10:nth-child(4) > .font-weight-normal").click()
    # 12 | click | id=submit_5 | 
    self.driver.find_element(By.ID, "submit_5").click()
    # 13 | click | css=#my_row_6 .mb-10:nth-child(2) > .font-weight-normal | 
    self.driver.find_element(By.CSS_SELECTOR, "#my_row_6 .mb-10:nth-child(2) > .font-weight-normal").click()
    # 14 | click | id=submit_6 | 
    self.driver.find_element(By.ID, "submit_6").click()
    # 15 | click | css=#my_row_7 .mb-10:nth-child(2) > .font-weight-normal | 
    self.driver.find_element(By.CSS_SELECTOR, "#my_row_7 .mb-10:nth-child(2) > .font-weight-normal").click()
    # 16 | click | id=submit_7 | 
    self.driver.find_element(By.ID, "submit_7").click()
    # 17 | click | css=#my_row_8 .mb-10:nth-child(2) > .font-weight-normal | 
    self.driver.find_element(By.CSS_SELECTOR, "#my_row_8 .mb-10:nth-child(2) > .font-weight-normal").click()
    # 18 | click | id=submit_8 | 
    self.driver.find_element(By.ID, "submit_8").click()
    # 19 | click | css=#my_row_9 .mb-10:nth-child(2) > .font-weight-normal | 
    self.driver.find_element(By.CSS_SELECTOR, "#my_row_9 .mb-10:nth-child(2) > .font-weight-normal").click()
    # 20 | click | id=submit_9 | 
    self.driver.find_element(By.ID, "submit_9").click()
    # 21 | click | css=#my_row_10 .mb-10:nth-child(5) > .font-weight-normal | 
    self.driver.find_element(By.CSS_SELECTOR, "#my_row_10 .mb-10:nth-child(5) > .font-weight-normal").click()
    # 22 | click | id=submit_10 | 
    self.driver.find_element(By.ID, "submit_10").click()
  
