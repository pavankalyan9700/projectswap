from selenium.webdriver.common.by import By


class login_admin_page:
  text_box_username_id = "user-name"
  text_box_password_id = "password"
  click_button_Xpath= "//input[@name= 'login-button']"


  def __init__(self,driver):
      self.driver=driver

  def enter_username(self,username):
      self.driver.find_element(By.ID,self.text_box_username_id).send_keys(username)

  def enter_password(self,password):
      self.driver.find_element(By.ID,self.text_box_password_id).send_keys(password)

  def click_login_button(self):
      self.driver.find_element(By.XPATH, self.click_button_Xpath).click()






