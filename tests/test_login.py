import pytest
import json
from pages.login_page import LoginPage

def load_users():
    with open("data/test_data.json") as f:
        data = json.load(f)
    return data["users"]

@pytest.mark.parametrize("user", load_users())
def test_login(page, user):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(user["username"], user["password"])
    if user["username"] == "locked_out_user":
        assert login_page.error_message.is_visible()
    else:
        assert page.url == "https://www.saucedemo.com/inventory.html"