import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.login_admin_page import login_admin_page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from base_pages.Place_Order_Page import Place_Order
from base_pages.Place_order_Page2 import Place_Order2


class Test_02_Place_Order:
    admin_page_url = Read_Config.admin_page_url()
    username = Read_Config.username()
    password = Read_Config.password()
    invalid_username = Read_Config.invalid_username()
    logger = Log_Maker.log_gen()

    def test_place_order(self, setup):
        self.logger.info("***********Test_03_Add_New_Customer started ***********")
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.admin_page_url)

        self.admin_lp = login_admin_page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login_button()
        time.sleep(5)

        self.driver.maximize_window()
        self.logger.info("***********Login completed ***********")
        self.logger.info("***********placing order ***********")


        self.place_order2 = Place_Order2(self.driver)
        self.place_order2.order_add_to_cart()
        self.place_order2.click_add_to_cart_icon()

        self.place_order2.click_on_remove()
        time.sleep(5)

        self.place_order2.click_on_continue_shopping()
        # self.place_order2.click_on_remove1()
        self.place_order2.order_adding_to_cart2()
        self.place_order2.click_adding_to_cart_icon_again()

        self.place_order2.click_button_checkout()
        self.place_order2.enter_first_name("pavankalyan")
        self.place_order2.enter_last_name("sonta")
        self.place_order2.enter_postal_code("500081")
        self.place_order2.click_continue()
        self.place_order2.click_finish()
        self.driver.close()







