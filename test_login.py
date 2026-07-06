import pytest
from playwright.sync_api import Page

@pytest.fixture
def open_site(page: Page):
    page.goto("https://www.saucedemo.com/")
    return page

def test_successful_login(open_site):
    page = open_site
    page.fill('[data-test="username"]', "standard_user")
    page.fill('[data-test="password"]', "secret_sauce")
    page.click('[data-test="login-button"]')
    assert page.url == "https://www.saucedemo.com/inventory.html"

def test_no_valid_login(open_site):
    page = open_site
    page.fill('[data-test="username"]', "wrong_user")
    page.fill('[data-test="password"]', "wrong")
    page.click('[data-test="login-button"]')
    error = page.locator('[data-test="error"]')
    assert error.is_visible()
    assert "do not match" in error.text_content()

def test_empty_login(open_site):
    page = open_site
    page.click('[data-test="login-button"]')
    error = page.locator('[data-test="error"]')
    assert error.is_visible()
    assert "Username is required" in error.text_content()

def test_empty_password(open_site):
    page = open_site
    page.fill('[data-test="username"]', "standard_user")
    page.click('[data-test="login-button"]')
    error = page.locator('[data-test="error"]')
    assert error.is_visible()
    assert "Password is required" in error.text_content()