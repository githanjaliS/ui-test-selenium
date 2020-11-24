from selenium import webdriver
from testBase.testBase import TestBase
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
import time

	



class TestReliencePage():
	'''
	doc string
	'''
	url = "https://www.reliancedigital.in/"

	def openPage(self):

		self.driver = TestBase.initialisationDriver(self.url)
		self.driver.implicitly_wait(30)
		

	#Locators with Actions	

	def searchItem(self, item):
		driver = self.driver
		self.driver.implicitly_wait(30)
		self.driver.find_element_by_id("suggestionBoxEle").send_keys(item)
		

	def buttonClick(self):
		driver = self.driver
		self.driver.implicitly_wait(30)
		self.driver.find_element_by_id("RIL_HomeSearchButton").click()
		

	def assertItem(self):
		driver = self.driver
		self.driver.implicitly_wait(30)
		self.driver.find_element_by_xpath("//p[contains(text(),'Apple iPhone XR 64 GB, Yellow (Includes Earpods an')]")
		return True
		
		
	def findValue(self):
		driver = self.driver
		self.driver.implicitly_wait(30)
		self.find_price = self.driver.find_element_by_xpath("//body/div[@id='root']/main[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/ul[1]/li[1]/div[1]/a[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]")
		#print(self.find_price.text)	
		return self.find_price

	def tearDown(self):
		driver = self.driver
		self.driver.quit()			




