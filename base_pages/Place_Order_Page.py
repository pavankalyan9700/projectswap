import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Place_Order:

  clicking_lets_talk_button = "//button[@class='mktoButton']"
  checking_box = "//label[@id='LblmktoCheckbox_47266_0']"
  clicking_on_dropdown =  "//select[@data-test='product-sort-container']"
  clicks_on_dropdown_and_selects_options = "//select[@id='Solution_Interest__c']"
  order_adding_to_cart = "//button[@id='add-to-cart-sauce-labs-backpack']"
  click_adding_to_cart_icon = "//a[@class='shopping_cart_link']"
  clicking_button_checkout = "//button[@id='checkout']"
  entering_first_name = "//input[@id='first-name']"
  entering_last_name = "//input[@id='last-name']"
  entering_postal_code = "//input[@id='postal-code']"
  clicking_continue = "//input[@id='continue']"
  clicking_finish = "//button[@id='finish']"
  clicking_menu = "//button[@id='react-burger-menu-btn']"
  clicking_about = "//a[@id='about_sidebar_link']"
  verified_title_text = "//p[text()='Introducing Sauce AI: Intelligent Agents for Next-Gen Software Quality']"
  # scrolling_and_clickings = "//a[.//span[normalize-space()='Sauce Web Testing']]"

  scrolling_and_clicking = "//button[.//text()[normalize-space()='Learn more about integrations']]"
  clicking_demo = "//button[.//text()[normalize-space()='Book a demo']]"
  entered_email = "//input[@id='Email']"
  entered_company = "//input[@id='Company']"




  def __init__(self,driver):
      self.driver=driver


  def select_from_dropdown(self, visible_text):
      dropdown = Select(self.driver.find_element(By.XPATH, self.clicking_on_dropdown))
      dropdown.select_by_visible_text(visible_text)

  def order_add_to_cart(self):
      self.driver.find_element(By.XPATH,self.order_adding_to_cart).click()

  def click_add_to_cart_icon(self):
      self.driver.find_element(By.XPATH,self.click_adding_to_cart_icon).click()

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


  def click_menu(self):
      self.driver.find_element(By.XPATH, self.clicking_menu).click()


  def click_about(self):
      self.driver.find_element(By.XPATH, self.clicking_about).click()

  def verify_title_text(self):
      return self.driver.find_element(
          By.XPATH, self.verified_title_text
      ).text

  def click_on_book_a_demo(self):
      wait = WebDriverWait(self.driver, 15)

      book_demo_btn = wait.until(
          EC.element_to_be_clickable(
              (By.XPATH, self.clicking_demo)
          )
      )

      book_demo_btn.click()

  def switch_to_new_window(self, timeout=10):
      # Wait until a second window is available
      WebDriverWait(self.driver, timeout).until(
          lambda d: len(d.window_handles) > 1
      )
      # Switch to the new window
      self.driver.switch_to.window(self.driver.window_handles[1])


  def talk_email(self):
      self.driver.find_element(By.XPATH, self.entered_email).send_keys("pavan@gmail.com")

  def talk_company(self):
      self.driver.find_element(By.XPATH, self.entered_company).send_keys("channel soft")


  def clicks_on_dropdown_and_selects_option(self, visible_text):
      dropdown = Select(self.driver.find_element(By.XPATH, self.clicks_on_dropdown_and_selects_options))
      dropdown.select_by_visible_text(visible_text)

  def click_on_check_box(self):
      self.driver.find_element(By.XPATH, self.checking_box).click()

  def click_on_lets_talk_button(self, timeout=10):
      WebDriverWait(self.driver, timeout).until(
          EC.element_to_be_clickable((By.XPATH, self.clicking_lets_talk_button))
      ).click()










  # def scroll_and_click(self):
  #     element = self.driver.find_element(By.XPATH, self.scrolling_and_clicking)
  #
  #     self.driver.execute_script(
  #         "arguments[0].scrollIntoView({behavior:'smooth', block:'center'});",
  #         element
  #     )
  #     element.click()





# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# def scroll_and_click(self):
#     wait = WebDriverWait(self.driver, 15)
#
#     element = wait.until(
#         EC.presence_of_element_located(
#             (By.XPATH, self.scrolling_and_clicking)
#         )
#     )
#
#     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)
#     # Scroll to element
#     self.driver.execute_script(
#         "arguments[0].scrollIntoView({behavior:'smooth', block:'center'});",
#         element
#     )
#
#     # Small wait to allow scroll animation
#     self.driver.implicitly_wait(1)
#
#     # Click using JS (MOST RELIABLE)
#     self.driver.execute_script("arguments[0].click();", element)


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scroll_and_click(self):
    wait = WebDriverWait(self.driver, 20)

    # 1️⃣ Scroll fully to bottom FIRST
    self.driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);"
    )
    time.sleep(3)  # footer lazy load

    # 2️⃣ NOW locate element (clickable)
    element = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, self.scrolling_and_clicking)
        )
    )

    print("URL:", self.driver.current_url)
    print("Element text:", element.text)

    # 3️⃣ Bring element to center
    self.driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        element
    )
    time.sleep(1)

    # 4️⃣ Click using JS (React-safe)
    self.driver.execute_script("arguments[0].click();", element)




