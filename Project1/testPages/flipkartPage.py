from selenium import webdriver
from testBase.testBase import TestBase
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager




class TestFlipkartPage():
	'''
	doc string
	'''
	url = "https://www.flipkart.com"
	

	def openPage(self):

		self.driver = TestBase.initialisationDriver(self.url)
		self.driver.implicitly_wait(30)
		

	#Locators and Actions	


	def closeSignupWindow(self):
		driver = self.driver
		self.driver.implicitly_wait(30)
		assert self.driver.find_element_by_xpath("//button[contains(text(),'✕')]")
		self.driver.find_element_by_xpath("//button[contains(text(),'✕')]").click()

	def searchItem(self, item):
		driver = self.driver
		self.driver.implicitly_wait(30)
		self.driver.find_element_by_xpath("//body/div[@id='container']/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/input[1]").send_keys(item)

	def buttonClick(self):
		driver = self.driver
		self.driver.implicitly_wait(30)
		self.driver.find_element_by_xpath("//body/div[@id='container']/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/button[1]/*[1]").click()

	def assertItem(self):
		driver = self.driver
		self.driver.implicitly_wait(30)
		self.driver.find_element_by_xpath("//div[contains(text(),'Apple iPhone XR (Yellow, 64 GB) (Includes EarPods,')]")
		return True

	def findValue(self):
		driver = self.driver
		self.driver.implicitly_wait(30)
		self.find_price = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[2]/div/div[2]/div[2]/div/div/div/a/div[2]/div[2]/div[1]/div/div[1]')
		return self.find_price
		
	def tearDown(self):
		driver = self.driver
		self.driver.quit()
