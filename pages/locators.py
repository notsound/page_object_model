from selenium.webdriver.common.by import By

class MainPageLocators(object):
	ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
	PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main>h1")
	ITEM_ADDED_PHRASE = (By.CSS_SELECTOR, "div.alertinner")
	NOTIFY_PRODUCT_NAME = (By.CSS_SELECTOR, "div.alertinner>strong")
	COST_IN_NOTIFY = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info.fade.in>div>p:nth-child(1)>strong")
	ITEM_PRICE = (By.CSS_SELECTOR, "div.product_main>p.price_color")
	GO_TO_BASKET = (By.CSS_SELECTOR, "div.basket-mini>span>a.btn-default")

class LoginPageLocators(object):
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
	EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
	PASSWD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
	CONFIRM_PASSWD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
	REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form>button")

class BasePageLocators(object):
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
	BASKET_BUTTON = (By.CSS_SELECTOR, "div>div.basket-mini.pull-right.hidden-xs>span>a")
	EMPTY_PHRASE = (By.CSS_SELECTOR, "#content_inner>p")
	BASKET_FORMSET = (By.CSS_SELECTOR, "#basket_formset")
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")