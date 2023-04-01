from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

def simple_alert_test():

	# Choose Simple Alert tab
	alert_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='#example-1-tab-1']")))
	time.sleep(2)
	alert_btn.click()
	time.sleep(2)

	# Switch to the iframe where the alert button is located
	iframe = wait.until(EC.presence_of_element_located((By.XPATH, '//iframe[@src="alert/simple-alert.html"]')))
	driver.switch_to.frame(iframe)

	# Locate the alert button by its XPath and click on it
	button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'alert box')]")))
	time.sleep(2)
	button.click()
	time.sleep(2)

	# Switch to the alert and get the text from it
	alert = Alert(driver)
	time.sleep(2)
	alert_text = alert.text
	time.sleep(2)

	# Verify the text based on the expected text value
	expected_text = "I am an alert box!"
	assert alert_text == expected_text, f"Simple Alert text did not match expected text: {expected_text}"
	if alert_text == expected_text:
		print("Simple Alert match with the expected text!")

	# Accept the alert to close it
	alert.accept()
	time.sleep(5)

def input_alert_test():
	# Choose Input Alert tab
	alert_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='#example-1-tab-2']")))
	time.sleep(2)
	alert_btn.click()
	time.sleep(2)

	# Switch to the iframe where the alert button is located
	iframe = wait.until(EC.presence_of_element_located((By.XPATH, '//iframe[@src="alert/input-alert.html"]')))
	driver.switch_to.frame(iframe)

	# Locate the alert button by its XPath and click on it
	button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Input box')]")))
	time.sleep(2)
	button.click()
	time.sleep(2)

	# Move to alert prompt window and set a new value, then click OK
	input_value = "John Doe"
	alert = Alert(driver)
	time.sleep(2)
	alert.send_keys(input_value)
	alert.accept()
	time.sleep(2)

	# Get the new output
	alert_text = wait.until(EC.element_to_be_clickable((By.ID, "demo"))).text

	# Verify the text based on the expected text value
	expected_text = f"Hello {input_value}! How are you today?"
	assert alert_text == expected_text, f"Alert text did not match expected text: {expected_text}"
	if alert_text == expected_text:
		print("Input Alert match with the expected text!")

	time.sleep(5)

try:
	# Create a new instance of a Chrome driver
	driver = webdriver.Chrome()
	driver.maximize_window()

	# Navigate to the URL
	driver.get("https://www.way2automation.com/way2auto_jquery/alert.php#load_box")

	wait = WebDriverWait(driver, 10)
	simple_alert_test()
	driver.switch_to.default_content()
	input_alert_test()

except Exception as e:
    # handle the exception here (print an error message, log the error, etc.)
    print("An error occurred:", e)

finally:
    print("----- ALL TESTS ARE PASSED! -----")
    # always close the webdriver instance to free up system resources
    driver.quit()