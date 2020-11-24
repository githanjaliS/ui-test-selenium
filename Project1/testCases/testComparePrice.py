from selenium import webdriver
from re import sub
from _decimal import Decimal
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from testPages.reliencePage import TestReliencePage
from testPages.flipkartPage import TestFlipkartPage
from testUtils.baseUtils import BaseUtils
import pytest


class TestFirst(object):
	'''
	Test to compare the price value of an item between 2 commercial websites
	:author: @githanjalis
	'''

	def testComparePrice(self):
		item = 'iPhone XR (64GB) - Yellow'
		'''
		Calling methods from TestReliencePage to perform the Action of extracting price value from web elements
		of Relience Digital
		'''
		product_in_Rel = TestReliencePage()
		product_in_Rel.openPage() #opens the webpage
		product_in_Rel.searchItem(item) #prints the item search panle
		product_in_Rel.buttonClick() #clicks on search_button to perform search action
		assert product_in_Rel.assertItem() #asserts if the item exists
		self.prod_reli_value = product_in_Rel.findValue() #returns the price value of the item
		price_in_rel = BaseUtils.BaseUserUtils.extractValue(self.prod_reli_value.text) #convert and extract int value from string to comparision
		
		'''
		Calling methods from TestReliencePage to perform the Action of extracting price value from web elements
		of Flipkart
		'''
		product_in_flip = TestFlipkartPage()
		product_in_flip.openPage() #opens the webpage
		product_in_flip.closeSignupWindow() #asserts the sign up window abd closes it if true
		product_in_flip.searchItem(item) #prints the item search panle
		product_in_flip.buttonClick() #clicks on search_button to perform search action
		assert product_in_flip.assertItem() #asserts if the item exists
		self.prod_flip_value = product_in_flip.findValue() #returns the price value of the item
		price_in_flip = BaseUtils.BaseUserUtils.extractValue(self.prod_flip_value.text) #convert and extract int value from string to comparision
		
		#prints the price of items
		print("Price of {} in Relience Digital is {}".format(item,self.prod_reli_value.text))
		print("Price of {} in Flipkart is {}".format(item,self.prod_flip_value.text))

		#price comparision to find the website selling the item in a comparitively lesser value
		if price_in_rel > price_in_flip:
			print("cheapest in flipkart")
		else:	
			print("cheapest in Relience")

		#driver exit method	
		product_in_Rel.tearDown()
		product_in_flip.tearDown()

		





		








	









