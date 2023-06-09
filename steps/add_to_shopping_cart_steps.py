from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('I am logged in as "{username}" with password "{password}"')
def step_given_logged_in(context, username, password):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")
    context.driver.find_element(By.ID, "user-name").send_keys(username)

    time.sleep(2)
    context.driver.find_element(By.ID, "password").send_keys(password)
    
    time.sleep(2)
    context.driver.find_element(By.ID, "login-button").click()

# Scenario 1
@when('I select an item named "{item_name}"')
def step_when_select_item(context, item_name):
    context.driver.find_elements("name", item_name)

@when('I add the item to the shopping cart')
def step_when_add_to_cart(context):

    time.sleep(2)
    context.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

@then('the item is displayed in the shopping cart')
def step_then_item_displayed_in_cart(context):

    time.sleep(2)
    assert context.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").is_displayed()
    context.driver.quit()

# Scenario 2
@when('I add an item to the cart')
def add_item_to_cart(context):

    time.sleep(2)
    context.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

@when('I remove the item from the cart')
def remove_item_from_cart(context):

    time.sleep(2)
    context.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

@then('The item should be removed from the cart')
def verify_item_removed_from_cart(context):

    time.sleep(2)
    cart_badge = context.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    time.sleep(2)
    assert len(cart_badge) == 0

# Scenario 3
@when('I click on an item')
def click_on_item(context):

    time.sleep(2)
    item_link = context.driver.find_element(By.CLASS_NAME, "inventory_item_name")
    time.sleep(2)
    item_link.click()


@then('I should see the item details')
def verify_item_details(context):
    time.sleep(2)
    item_title = context.driver.find_element(By.CLASS_NAME, "inventory_details_name")
    time.sleep(2)
    assert item_title.is_displayed()

# Scenario 4
@when('I add items to the cart')
def add_items_to_cart(context):
    add_to_cart_buttons = context.driver.find_elements(By.XPATH, "//button[text()='ADD TO CART']")
    time.sleep(2)
    for button in add_to_cart_buttons:
        time.sleep(0.5)
        button.click()

@when('I empty the cart')
def empty_cart(context):
    cart_button = context.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    time.sleep(2)
    cart_button.click()
    remove_buttons = context.driver.find_elements(By.XPATH, "//button[text()='REMOVE']")
    time.sleep(2)
    for button in remove_buttons:
        time.sleep(0.5)
        button.click()

@then('The cart should be empty')
def verify_cart_empty(context):
    time.sleep(2)
    cart_items = context.driver.find_elements(By.CLASS_NAME, "cart_item")
    time.sleep(2)
    assert len(cart_items) == 0

# Scenario 5
@when('I proceed to checkout')
def proceed_to_checkout(context):
    time.sleep(2)
    cart_button = context.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    time.sleep(2)
    cart_button.click()
    time.sleep(2)
    checkout_button = context.driver.find_element(By.ID, "checkout")
    time.sleep(2)
    checkout_button.click()


@then('I should be redirected to the checkout page')
def verify_checkout_page(context):
    time.sleep(2)
    checkout_title = context.driver.find_element(By.CLASS_NAME, "title").text
    time.sleep(2)
    assert checkout_title == "Checkout: Your Information"


# USER? standard_user
# PASS? secret_sauce
# site https://www.saucedemo.com/