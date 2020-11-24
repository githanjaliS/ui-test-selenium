from selenium import webdriver
from testBase.testBase import TestBase
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
import time

	



class TestReliencePage():
	'''
	This file contains the elements of the page www.relience.in and can be used as driver calls in the test functions
	'''
	url = "https://www.reliancedigital.in/"

	def openPage(self):

		self.driver = TestBase.initialisationDriver(self.url)
		self.driver.implicitly_wait(30)# Wait implicitly for elements to be ready before attempting interactions
		

	#Locators with Actions	

	#Locate the search tab and enter and item
	def searchItem(self, item):
		driver = self.driver
		self.driver.implicitly_wait(30)# Wait implicitly for elements to be ready before attempting interactions
		self.driver.find_element_by_id("suggestionBoxEle").send_keys(item)
		
	#locate the serch button and click to contiue the search of the above entered item
	def buttonClick(self):
		driver = self.driver
		self.driver.implicitly_wait(30)# Wait implicitly for elements to be ready before attempting interactions
		self.driver.find_element_by_id("RIL_HomeSearchButton").click()
		
	#validate the item/XPATH present
	def assertItem(self):
		driver = self.driver
		self.driver.implicitly_wait(30)# Wait implicitly for elements to be ready before attempting interactions
		self.driver.find_element_by_xpath("//p[contains(text(),'Apple iPhone XR 64 GB, Yellow (Includes Earpods an')]")
		return True
		
	#Find the price value of an item by xpath	
	def findValue(self):
		driver = self.driver
		self.driver.implicitly_wait(30)# Wait implicitly for elements to be ready before attempting interactions
		self.find_price = self.driver.find_element_by_xpath("//body/div[@id='root']/main[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/ul[1]/li[1]/div[1]/a[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]")
		#print(self.find_price.text)	
		return self.find_price

	#driver exit method	
	def tearDown(self):
		driver = self.driver
		self.driver.quit()			




