from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.XPATH, '//form[@id="login_form"]')
    REGISTER_FORM = (By.XPATH, '//form[@id="register_form"]')


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.XPATH, '//button[contains(@class, "add-to-basket")]')
    PRODUCT_NAME = (By.XPATH, '//div[contains(@class, "main")]//h1')
    PRODUCT_PRICE = (By.XPATH, '//p[contains(@class, "price")]')
    SUCCESS_ADD_MSG = (By.XPATH, '(//div[@id="messages"]//div[@class="alertinner "])[1]')
    BASKET_PRICE_MSG = (By.XPATH, '(//div[@id="messages"]//div[@class="alertinner "])[3]')
