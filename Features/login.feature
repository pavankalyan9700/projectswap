#Feature: Admin Login Functionality
#
#  Scenario: Verify admin page title
#    Given the admin login page is open
#    When I check the page title
#    Then the title should be "Swag Labs"
#
#  Scenario: Login with valid credentials
#    Given the admin login page is open
#    When I enter valid username and password
#    And I click the login button
#    Then I should see the dashboard with text "Swag Labs"
#
#
#  Scenario: Login with invalid credentials
#    Given the admin login page is open
#    When I enter invalid username and valid password
#    And I click the login button
#    Then I should see the error message "Epic sadface: Username and password do not match any user in this service"
Feature: Place order after successful login

  Scenario: Login and place an order successfully

      Given user is logged into the application
        When user clicks on menu button
        And user click on about button
        Then user should see the title text
#        When user scrolls down and clicks on the element
        When user clicks on book a demo
        And user switch to new window
        And user enter email
        And user enter company
        And user clicks on dropdown and selects "Scalable Test Automation"
        And user click on check box
        And user selects on lets talk
#        When user clicks on dropdown and selects "Price (high to low)"
#        And user adds product to cart
#        And user completes checkout with valid details
#        Then order should be placed successfully




