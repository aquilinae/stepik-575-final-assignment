import pytest

from pages.product_page import ProductPage

LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


@pytest.mark.parametrize('link', [f'{LINK}?promo=offer{i}' for i in range(10)])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_added_to_basket(product_name=page.product_name, product_price=page.product_price)
