from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators(BasePageLocators):
    ...


class LoginPageLocators(BasePageLocators):
    LOGIN_FORM = (By.XPATH, '//form[@id="login_form"]')
    REGISTER_FORM = (By.XPATH, '//form[@id="register_form"]')


class ProductPageLocators(BasePageLocators):
    ADD_TO_BASKET_BTN = (By.XPATH, '//button[contains(@class, "add-to-basket")]')
    PRODUCT_NAME = (By.XPATH, '//div[contains(@class, "main")]//h1')
    PRODUCT_PRICE = (By.XPATH, '//p[contains(@class, "price")]')
    SUCCESS_ADD_MSG = (By.XPATH, '(//div[@id="messages"]//div[@class="alertinner "])[1]')
    BASKET_PRICE_MSG = (By.XPATH, '(//div[@id="messages"]//div[@class="alertinner "])[3]')
