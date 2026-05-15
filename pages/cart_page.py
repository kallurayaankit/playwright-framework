from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.locator("#checkout")
        self.cart_items = page.locator(".cart_item")

    def proceed_to_checkout(self):
        self.checkout_button.click()

    def remove_product(self, product_name: str):
        item = self.cart_items.filter(has_text=product_name)
        item.locator("button", has_text="Remove").click()