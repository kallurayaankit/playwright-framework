from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.shopping_cart_link = page.locator(".shopping_cart_link")
        self.product_sort = page.locator("[data-test='product_sort_container']")

    def add_product_to_cart(self, product_name: str):
        product_item = self.page.locator(".inventory_item", has_text=product_name)
        add_button = product_item.locator("button", has_text="Add to cart")
        add_button.click()

    def go_to_cart(self):
        self.shopping_cart_link.click()