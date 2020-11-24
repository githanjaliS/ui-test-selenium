from re import sub
from decimal import Decimal
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

class MyClass(object):
	'''
	classdocs
	'''
	def setupClass(self):
		self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options = chrome_options)

	def getPriceRelience(self, url):
		driver = self.driver
		driver.delete_all_cookies();
		driver.implicitly_wait(60)
		driver.maximize_window();
		driver.get(url)
		driver.find_element_by_id("suggestionBoxEle").send_keys("iPhone XR (64GB) - Yellow")
		driver.find_element_by_id("RIL_HomeSearchButton").click()
		driver.implicitly_wait(30)

		if driver.find_element_by_xpath("//p[contains(text(),'Apple iPhone XR 64 GB, Yellow (Includes Earpods an')]"):
			print("Match Found")

		price = driver.find_element_by_xpath("//body/div[@id='root']/main[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/ul[1]/li[1]/div[1]/a[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]").text
		new_price = extractValue(price)	
		return new_price

	def getPriceflipkart(self, url):
		driver = self.driver
		driver.delete_all_cookies();
		driver.implicitly_wait(60)
		driver.maximize_window();
		driver.get(url)
		driver.implicitly_wait(30)
		
		if driver.find_element_by_xpath("//button[contains(text(),'✕')]"):
			driver.find_element_by_xpath("//button[contains(text(),'✕')]").click()
		
		driver.find_element_by_xpath("//body/div[@id='container']/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/input[1]").send_keys("iPhone XR (64GB) - Yellow")
		driver.find_element_by_xpath("//body/div[@id='container']/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/button[1]/*[1]").click()
		
		if driver.find_element_by_xpath("//div[contains(text(),'Apple iPhone XR (Yellow, 64 GB) (Includes EarPods,')]"):
			print("found")

		price = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[2]/div/div[2]/div[2]/div/div/div/a/div[2]/div[2]/div[1]/div/div[1]').text
		new_price = extractValue(price)	
		return new_price

	def tearDown(self):
		self.driver.quit()

	def __init__(self):
		'''
		constructor
		'''
		print("\nStarting my first selenium project")


#### Driver Code#####

def extractValue(price):
	value = Decimal(sub(r'[^\d.]', '', price))
	return value
url1 = "https://www.reliancedigital.in/"
url2 = "https://www.flipkart.com"

myclass = MyClass()
myclass.setupClass()

x = myclass.getPriceRelience(url1)
y = myclass.getPriceflipkart(url2)
print("Price in Relience:", x)
print("Price in Flipkart:", y)
if x > y:
	print("Cheapest in Flipkart")
else:
	print("Cheapest in Relience")


myclass.tearDown()	


