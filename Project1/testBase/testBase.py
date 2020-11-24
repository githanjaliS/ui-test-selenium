from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

class TestBase(object):
	'''
	doc string
	'''

	def __init__(self):
		'''
		constructor
		'''


	def initialisationDriver(url):
		driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options = chrome_options)
		driver.delete_all_cookies();
		driver.maximize_window();
		driver.get(url)
		return driver

	#def implicitly_wait(self,)



		
		