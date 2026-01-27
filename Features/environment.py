# from selenium import webdriver
#
# def before_scenario(context, scenario):
#     context.driver = webdriver.Chrome()
#
# def after_scenario(context, scenario):
#     context.driver.quit()

from selenium import webdriver

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()

def after_scenario(context, scenario):
    context.driver.quit()


import os

def after_scenario(context, scenario):
    if scenario.status == "failed":
        screenshots_dir = "screenshots"
        os.makedirs(screenshots_dir, exist_ok=True)

        screenshot_name = scenario.name.replace(" ", "_") + ".png"
        screenshot_path = os.path.join(screenshots_dir, screenshot_name)

        context.driver.save_screenshot(screenshot_path)

        print(f"\nSCREENSHOT SAVED AT: {screenshot_path}")

    context.driver.quit()

import allure
import os

def after_scenario(context, scenario):
    if scenario.status == "failed":
        screenshot_path = "screenshots/" + scenario.name.replace(" ", "_") + ".png"
        context.driver.save_screenshot(screenshot_path)

        with open(screenshot_path, "rb") as image:
            allure.attach(
                image.read(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

    context.driver.quit()
