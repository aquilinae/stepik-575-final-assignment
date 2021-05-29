from pages.product_page import ProductPage


LINK = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_added_to_basket(product_name=page.product_name, product_price=page.product_price)