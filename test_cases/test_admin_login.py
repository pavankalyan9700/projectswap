import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.login_admin_page import login_admin_page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker

class Test_01_Admin_Login:

    admin_page_url = Read_Config.admin_page_url()
    username = Read_Config.username()
    password = Read_Config.password()
    invalid_username = Read_Config.invalid_username()
    logger= Log_Maker.log_gen()

    def test_title_verification(self,setup):
        self.logger.info("**********************Test_01_Admin_Login******************************")
        self.logger.info("**********************test_title_verification******************************")



        self.driver = setup
        self.driver.get(self.admin_page_url)

        act_title = self.driver.title
        exp_title = "Swag Labs"

        if act_title == exp_title:
            self.logger.info("**********************test_title_verification******************************")

            assert True
            self.driver.close()
        else:
            # self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.driver.close()
            assert False

    def test_valid_admin_login(self,setup):
        self.logger.info("**********************test_valid_admin_login******************************")

        self.driver = setup
        self.driver.get(self.admin_page_url)

        self.admin_lp = login_admin_page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login_button()

        act_dashboard_text = self.driver.find_element(
            By.XPATH, "//div[@class='app_logo']"
        ).text

        if act_dashboard_text == "Swag Labs":
            self.logger.info("**********************test_valid_admin_login******************************")

            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
            self.driver.close()
            assert False


    def test_invalid_admin_login(self,setup):
        self.logger.info("**********************test_invalid_admin_login******************************")

        self.driver = setup
        self.driver.get(self.admin_page_url)

        self.admin_lp = login_admin_page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login_button()

        error_message = self.driver.find_element(
            By.XPATH, "//h3[@data-test='error']").text

        if error_message == "Epic sadface: Username and password do not match any user in this service":
            self.logger.info("**********************test_invalid_admin_login******************************")

            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
            self.driver.close()
            assert False


