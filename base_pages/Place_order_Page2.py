from selenium.webdriver.common.by import By


class Place_Order2:

  order_adding_to_cart = "//button[@id='add-to-cart-sauce-labs-backpack']"
  click_adding_to_cart_icon = "//a[@class='shopping_cart_link']"

  clicking_on_remove= "//button[@id= 'remove-sauce-labs-backpack']"
  clicking_on_continue_shopping = "//button[@id= 'continue-shopping']"
  # clicking_on_remove1 = "//button[@id= 'remove-sauce-labs-backpack']"
  ordering_adding_to_cart2= "//button[@id= 'add-to-cart-sauce-labs-bike-light']"
  clicking_adding_to_cart_icon_again = "//a[@class='shopping_cart_link']"

  clicking_button_checkout = "//button[@id='checkout']"
  entering_first_name = "//input[@id='first-name']"
  entering_last_name = "//input[@id='last-name']"
  entering_postal_code = "//input[@id='postal-code']"
  clicking_continue = "//input[@id='continue']"
  clicking_finish = "//button[@id='finish']"


  def __init__(self,driver):
      self.driver=driver

  def order_add_to_cart(self):
      self.driver.find_element(By.XPATH,self.order_adding_to_cart).click()

  def click_add_to_cart_icon(self):
      self.driver.find_element(By.XPATH,self.click_adding_to_cart_icon).click()



  def click_on_remove(self):
      self.driver.find_element(By.XPATH,self.clicking_on_remove).click()

  def click_on_continue_shopping(self):
      self.driver.find_element(By.XPATH,self.clicking_on_continue_shopping).click()


  def click_on_remove1(self):
      self.driver.find_element(By.XPATH,self.clicking_on_remove1).click()


  def order_adding_to_cart2(self):
      self.driver.find_element(By.XPATH,self.ordering_adding_to_cart2).click()


  def click_adding_to_cart_icon_again(self):
      self.driver.find_element(By.XPATH,self.clicking_adding_to_cart_icon_again).click()




  def click_button_checkout(self):
      self.driver.find_element(By.XPATH, self.clicking_button_checkout).click()

  def enter_first_name(self,first_name):
      self.driver.find_element(By.XPATH, self.entering_first_name).send_keys(first_name)

  def enter_last_name(self, last_name):
      self.driver.find_element(By.XPATH, self.entering_last_name).send_keys(last_name)


  def enter_postal_code(self, postal_code):
      self.driver.find_element(By.XPATH, self.entering_postal_code).send_keys(postal_code)


  def click_continue(self):
      self.driver.find_element(By.XPATH, self.clicking_continue).click()


  def click_finish(self):
      self.driver.find_element(By.XPATH, self.clicking_finish).click()










