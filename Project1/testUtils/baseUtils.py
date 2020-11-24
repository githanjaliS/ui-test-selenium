from re import sub
from _decimal import Decimal
from selenium import webdriver

class BaseUtils(object):
	'''
	doc string
	'''
	class BaseUserUtils(object):

		@staticmethod
		def extractValue(price):
			price.encode('ascii', 'ignore').decode("utf-8")
			value = Decimal(sub(r'[^\d.]'r'', '', price))
			return value

