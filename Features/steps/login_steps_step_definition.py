import time

from behave import given, when, then
from selenium.webdriver.common.by import By
from base_pages.login_admin_page import login_admin_page
from base_pages.Place_Order_Page import Place_Order
from utilities.read_properties import Read_Config


@given("user is logged into the application")
def step_login(context):
    context.driver.get(Read_Config.admin_page_url())

    login_page = login_admin_page(context.driver)
    login_page.enter_username(Read_Config.username())
    login_page.enter_password(Read_Config.password())
    login_page.click_login_button()
    time.sleep(5)

    context.place_order = Place_Order(context.driver)


@when("user adds product to cart")
def step_add_product(context):
    context.place_order.order_add_to_cart()
    context.place_order.click_add_to_cart_icon()
    context.place_order.click_button_checkout()


@when("user completes checkout with valid details")
def step_checkout(context):
    context.place_order.enter_first_name("pavankalyan")
    context.place_order.enter_last_name("sonta")
    context.place_order.enter_postal_code("500081")
    context.place_order.click_continue()
    context.place_order.click_finish()


@then("order should be placed successfully")
def step_verify_order(context):
    success_text = context.driver.find_element(
        By.XPATH, "//h2[@class='complete-header']"
    ).text

    assert success_text == "Thank you for your order!"



@when('user clicks on dropdown and selects "Price (high to low)"')
def step_select_price_high_to_low(context):
    context.place_order.select_from_dropdown("Price (high to low)")


@when('user clicks on menu button')
def step_select_menu(context):
    context.place_order.click_menu()

@when('user click on about button')
def step_select_all_items(context):
    context.place_order.click_about()


@then('user should see the title text')
def step_verify_title(context):
    actual_text = context.place_order.verify_title_text()
    expected_text = "Introducing Sauce AI: Intelligent Agents for Next-Gen Software Quality"

    assert actual_text == expected_text


@when('user scrolls down and clicks on the element')
def step_scroll_and_click(context):
    context.place_order.scroll_and_click()


@when('user clicks on book a demo')
def step_click_on_book_a_demo(context):
    context.place_order.click_on_book_a_demo()

@when('user switch to new window')
def step_switch_to_new_window(context):
    context.place_order.switch_to_new_window()

@when('user click on check box')
def step_check_box(context):
    context.place_order.click_on_check_box()

@when('user enter email')
def step_enter_email(context):
    context.place_order.talk_email()

@when('user enter company')
def step_enter_company(context):
    context.place_order.talk_company()

@when('user clicks on dropdown and selects "Scalable Test Automation"')
def step_select_price_high_to_low(context):
    context.place_order.clicks_on_dropdown_and_selects_option("Scalable Test Automation")



@when('user selects on lets talk')
def step_select_lets_talk(context):
    context.place_order.click_on_lets_talk_button()





# from behave import given, when, then
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from base_pages.login_admin_page import login_admin_page
# from utilities.read_properties import Read_Config
#
# @given('the admin login page is open')
# def step_open_admin_page(context):
#     context.driver = webdriver.Chrome()
#     context.driver.get(Read_Config.admin_page_url())
#
# @when('I check the page title')
# def step_check_title(context):
#     context.act_title = context.driver.title
#
# @then('the title should be "{expected_title}"')
# def step_verify_title(context, expected_title):
#     assert context.act_title == expected_title
#     context.driver.quit()
#
# @when('I enter valid username and password')
# def step_enter_valid_credentials(context):
#     login_page = login_admin_page(context.driver)
#     login_page.enter_username(Read_Config.username())
#     login_page.enter_password(Read_Config.password())
#     context.login_page = login_page
#
# @when('I enter invalid username and valid password')
# def step_enter_invalid_credentials(context):
#     login_page = login_admin_page(context.driver)
#     login_page.enter_username(Read_Config.invalid_username())
#     login_page.enter_password(Read_Config.password())
#     context.login_page = login_page
#
# @when('I click the login button')
# def step_click_login(context):
#     context.login_page.click_login_button()
#
# @then('I should see the dashboard with text "{expected_text}"')
# def step_verify_dashboard(context, expected_text):
#     act_text = context.driver.find_element(By.XPATH, "//div[@class='app_logo']").text
#     assert act_text == expected_text
#     context.driver.quit()
#
# @then('I should see the error message "{expected_error}"')
# def step_verify_error(context, expected_error):
#     act_error = context.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
#     assert act_error == expected_error
#     context.driver.quit()
