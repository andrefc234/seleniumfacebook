from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Selenium WebDriver
browser = webdriver.Chrome()  # Make sure you have the Chrome WebDriver installed and in your PATH
browser.maximize_window()

try:
    # Open Facebook login page
    browser.get('https://www.facebook.com')

    # Enter credentials and log in
    email_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'email')))
    email_input.send_keys('your_email_here')  # Replace 'your_email_here' with your actual email

    password_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'pass')))
    password_input.send_keys('your_password_here')  # Replace 'your_password_here' with your actual password

    login_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Log In")]')))
    login_button.click()

    # Wait for navigation after login
    WebDriverWait(browser, 10).until(EC.url_changes)

    # You can add further actions here, such as navigating to a profile

except Exception as e:
    print('Bot encountered an error:', e)

finally:
    # Close the browser session
    browser.quit()
