import pytest
from playwright.sync_api import expect


@pytest.mark.passing
def test_search_for_a_product_verify_cross_sell_carousel_and_add_product_to_cart(set_up):
    search_term = "iPhone 13 64go"
    expected_number_of_results = 1
    page = set_up

    # Search for iPhone 11 64go and press enter
    page.locator('[data-qa=search-bar-input]').fill(search_term)
    page.keyboard.press('Enter')

    page.locator("[data-test='product-thumb']").first.click()

    page.locator("button[data-qa='product-page-buy-button-desktop']").click()

    page.locator("button[data-test='close-modal']").click()

    # Continue to cart
    page.locator('[data-qa="continue-shopping"]').click()

    # Assert if number of cross-sell product cards is greater than 1 (no direct method unlike TS, hence verifying
    # count not equal to 0 or 1)
    cross_sell_product_card = page.locator("div[data-qa='productCard']")
    expect(cross_sell_product_card).not_to_have_count(0)
    expect(cross_sell_product_card).not_to_have_count(1)

    # Assert if number of cart item is 1
    cart_items_before = page.locator("[data-test='cart-product']")
    expect(cart_items_before).to_have_count(expected_number_of_results)

    # Add an item from cross-sell to cart
    page.locator("li:nth-child(1) > span > div > a > div > div > button").click()

    # Assert if number of cart item is 2
    cart_items_after = page.locator("[data-test='cart-product']")
    expect(cart_items_after).to_have_count(2)
