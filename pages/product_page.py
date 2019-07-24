from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators


class StartPage(BasePage):
	def add_item_to_basket(self):	
		basket_button = self.browser.find_element(*MainPageLocators.ADD_TO_BASKET)
		basket_button.click()
		#return LoginPage(browser=self.browser, url=self.browser.current_url)

	def compare_book_name(self):
		book_name = self.browser.find_element(*MainPageLocators.PRODUCT_NAME).text
		actual_book_name = self.browser.find_element(*MainPageLocators.NOTIFY_PRODUCT_NAME).text
		assert self.is_element_present(*MainPageLocators.ITEM_ADDED_PHRASE), "Element is not presented"
		assert book_name == actual_book_name, "Book name do not match for page {}".format(self.url)

	def check_price(self):
		price = self.browser.find_element(*MainPageLocators.ITEM_PRICE).text
		notify_price = self.browser.find_element(*MainPageLocators.COST_IN_NOTIFY).text
		assert price == notify_price, "Price do not match"

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*MainPageLocators.ITEM_ADDED_PHRASE), "Success message is presented, but should not be"

	def element_is_disappeared(self):
		assert self.is_disappeared(*MainPageLocators.ITEM_ADDED_PHRASE), "Element is appeared"

