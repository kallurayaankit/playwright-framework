import pytest
import json
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@pytest.fixture
def logged_in_page(page):
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "secret_sauce")
    return page

def load_products():
    with open("data/test_data.json") as f:
        data = json.load(f)
    return data["products"]

@pytest.mark.parametrize("product", load_products())
def test_add_to_cart(logged_in_page, product):
    page = logged_in_page
    inventory = InventoryPage(page)
    inventory.add_product_to_cart(product)
    inventory.go_to_cart()
    cart = CartPage(page)
    assert cart.cart_items.filter(has_text=product).count() == 1