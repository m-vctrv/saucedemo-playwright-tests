import pytest
from playwright.sync_api import Page

@pytest.fixture
def login_add_to_cart(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.fill('[data-test="username"]', "standard_user")
    page.fill('[data-test="password"]', "secret_sauce")
    page.click('[data-test="login-button"]')
    page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    page.click('[data-test="shopping-cart-link"]')
    page.click('[data-test="checkout"]')
    return page

def test_happy_path(login_add_to_cart):
    page = login_add_to_cart
    page.fill('[data-test="firstName"]', "Misha")
    page.fill('[data-test="lastName"]', "Milka")
    page.fill('[data-test="postalCode"]', "123-123")
    page.click('[data-test="continue"]')
    checkout_ov = page.locator('[data-test="title"]')
    assert checkout_ov.text_content() == "Checkout: Overview"
    page.click('[data-test="finish"]')
    checkout_co = page.locator('[data-test="title"]')
    assert checkout_co.text_content() == "Checkout: Complete!"
