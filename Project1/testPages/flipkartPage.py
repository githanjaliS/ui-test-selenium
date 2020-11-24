from selenium import webdriver
from testBase.testBase import TestBase
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager




class TestFlipkartPage():
	'''
	This file contains the elements of the page www.flipkart.com and can be used as driver calls in the test functions
	'''
	url = "https://www.flipkart.com"
	

	def openPage(self):

		self.driver = TestBase.initialisationDriver(self.url)
		self.driver.implicitly_wait(30) # Wait implicitly for elements to be ready before attempting interactions
		

	#Locators and Actions	

	#Locate the signupwindow and close it by cllickig on X
	def closeSignupWindow(self):
		driver = self.driver
		self.driver.implicitly_wait(30)# Wait implicitly for elements to be ready before attempting interactions
		assert self.driver.find_element_by_xpath("//button[contains(text(),'✕')]")
		self.driver.find_element_by_xpath("//button[contains(text(),'✕')]").click()

	#Locate the search tab and enter and item
	def searchItem(self, item):
		driver = self.driver
		self.driver.implicitly_wait(30)# Wait implicitly for elements to be ready before attempting interactions
		self.driver.find_element_by_xpath("//body/div[@id='container']/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/input[1]").send_keys(item)

	#locate the serch button and click to contiue the search of the above entered item
	def buttonClick(self):
		driver = self.driver
		self.driver.implicitly_wait(30)# Wait implicitly for elements to be ready before attempting interactions
		self.driver.find_element_by_xpath("//body/div[@id='container']/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/button[1]/*[1]").click()

	#validate the item/XPATH present
	def assertItem(self):
		driver = self.driver
		self.driver.implicitly_wait(30)# Wait implicitly for elements to be ready before attempting interactions
		self.driver.find_element_by_xpath("//div[contains(text(),'Apple iPhone XR (Yellow, 64 GB) (Includes EarPods,')]")
		return True

	#Find the price value of an item by xpath
	def findValue(self):
		driver = self.driver
		self.driver.implicitly_wait(30)# Wait implicitly for elements to be ready before attempting interactions
		self.find_price = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[2]/div/div[2]/div[2]/div/div/div/a/div[2]/div[2]/div[1]/div/div[1]')
		return self.find_price

	#driver exit method		
	def tearDown(self):
		driver = self.driver
		self.driver.quit()
