import pytest
from playwright.sync_api import Page

@pytest.fixture
def login(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.fill('[data-test="username"]', "standard_user")
    page.fill('[data-test="password"]', "secret_sauce")
    page.click('[data-test="login-button"]')
    return page

def test_add_to_cart(login):
    page = login
    page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    cart_badge = page.locator('[data-test="shopping-cart-badge"]')
    assert cart_badge.text_content() == '1'

def test_remove_from_cart(login):
    page = login
    page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    page.click('[data-test="remove-sauce-labs-backpack"]')
    cart_badge = page.locator('[data-test="shopping-cart-badge"]')
    assert cart_badge.count() == 0

def test_active_filter(login):
    page = login
    page.select_option('[data-test="product-sort-container"]', value='lohi')
    active_option = page.locator('[data-test="active-option"]')
    assert active_option.text_content() == "Price (low to high)"

def test_check_cart(login):
    page = login
    page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    page.click('[data-test="shopping-cart-link"]')
    item_quantity = page.locator('[data-test="item-quantity"]')
    assert item_quantity.text_content() == "1"
    name_item = page.locator('[data-test="inventory-item-name"]')
    assert name_item.text_content() == "Sauce Labs Backpack"