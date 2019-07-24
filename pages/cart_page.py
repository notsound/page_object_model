from selenium import webdriver
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasePageLocators

class CartPage(BasePage):
	def basket_is_empty(self):
		assert self.is_element_present(*BasePageLocators.EMPTY_PHRASE), "Basket is not empty"

	def no_items_in_basket(self):
		assert self.is_not_element_present(*BasePageLocators.BASKET_FORMSET), "Basket has items"