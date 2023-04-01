from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def send_keys(xpath, new_value):
	element = wait.until(EC.visibility_of_element_located((By.XPATH, str(xpath))))
	element.send_keys(str(new_value))
	time.sleep(2)
	return element

def upload_file(xpath):
	# DEFINE YOUR LOCAL PATH HERE! <local_path>/MVP_TEST/Dummy/xxx.png
	file_path = "/Users/kennethsarashadi/Downloads/MVP_TEST/Dummy/cici.png"
	element = wait.until(EC.visibility_of_element_located((By.XPATH, str(xpath))))
	element.send_keys(str(file_path))
	time.sleep(2)

def select_value(xpath, selected_value):
	element = wait.until(EC.visibility_of_element_located((By.XPATH, str(xpath))))
	select = Select(element)
	select.select_by_value(str(selected_value))
	time.sleep(2)

def radio_button(xpath):
	element = wait.until(EC.visibility_of_element_located((By.XPATH, str(xpath)))).click()
	time.sleep(2)

def submit(xpath):
	element = wait.until(EC.visibility_of_element_located((By.XPATH, str(xpath)))).click()
	time.sleep(2)

def positive_test():
	# First Name
	send_keys("/html/body/section/div[1]/div/div/form/fieldset[1]/p[1]/input", "John Doe")

	# Last Name
	send_keys("/html/body/section/div[1]/div/div/form/fieldset[1]/p[2]/input", "Bourgess")

	# Marital Status
	radio_button("/html/body/section/div[1]/div/div/form/fieldset[2]/div/label[2]")

	# Hobby
	radio_button("/html/body/section/div[1]/div/div/form/fieldset[3]/div/label[3]/input")

	# Country
	select_value("/html/body/section/div[1]/div/div/form/fieldset[4]/select", "India")

	# DOB - Date
	select_value("/html/body/section/div[1]/div/div/form/fieldset[5]/div[1]/select", "1")

	# DOB - Month
	select_value("/html/body/section/div[1]/div/div/form/fieldset[5]/div[2]/select", "1")

	# DOB - Year
	select_value("/html/body/section/div[1]/div/div/form/fieldset[5]/div[3]/select", "2014")
	
	# Phone
	send_keys("/html/body/section/div[1]/div/div/form/fieldset[6]/input", "+49881122050")

	# Username
	uname = send_keys("/html/body/section/div[1]/div/div/form/fieldset[7]/input", "TESTER_QA_1")
	driver.execute_script("arguments[0].scrollIntoView();", uname)

	# Email
	send_keys("/html/body/section/div[1]/div/div/form/fieldset[8]/input", "tester@gmail.com")

	# Profile picture: Change the path here
	upload_file("/html/body/section/div[1]/div/div/form/fieldset[9]/input")

	# About
	send_keys("/html/body/section/div[1]/div/div/form/fieldset[10]/textarea", "I AM EXCITED")

	# Password 1
	send_keys("/html/body/section/div[1]/div/div/form/fieldset[11]/input", "Password@1")

	# Password 2
	send_keys("/html/body/section/div[1]/div/div/form/fieldset[12]/input", "Password@1")

	submit("/html/body/section/div[1]/div/div/form/fieldset[13]/input")

def negative_test():
	# First Name: BLANK

	# Last Name
	send_keys("/html/body/section/div[1]/div/div/form/fieldset[1]/p[2]/input", "Bourgess")

	# Marital Status
	radio_button("/html/body/section/div[1]/div/div/form/fieldset[2]/div/label[2]")

	# Hobby
	radio_button("/html/body/section/div[1]/div/div/form/fieldset[3]/div/label[3]/input")

	# Country
	select_value("/html/body/section/div[1]/div/div/form/fieldset[4]/select", "India")

	# DOB - Date
	select_value("/html/body/section/div[1]/div/div/form/fieldset[5]/div[1]/select", "1")

	# DOB - Month
	select_value("/html/body/section/div[1]/div/div/form/fieldset[5]/div[2]/select", "1")

	# DOB - Year
	select_value("/html/body/section/div[1]/div/div/form/fieldset[5]/div[3]/select", "2014")
	
	# Phone: BLANK

	# Username
	uname = send_keys("/html/body/section/div[1]/div/div/form/fieldset[7]/input", "TESTER_QA_1")
	driver.execute_script("arguments[0].scrollIntoView();", uname)

	# Email
	send_keys("/html/body/section/div[1]/div/div/form/fieldset[8]/input", "tester@gmail.com")

	# Profile picture: Change the path here
	upload_file("/html/body/section/div[1]/div/div/form/fieldset[9]/input")

	# About
	send_keys("/html/body/section/div[1]/div/div/form/fieldset[10]/textarea", "I AM EXCITED")

	# Password 1
	send_keys("/html/body/section/div[1]/div/div/form/fieldset[11]/input", "Password@1")

	# Password 2
	send_keys("/html/body/section/div[1]/div/div/form/fieldset[12]/input", "Password@1")

	submit("/html/body/section/div[1]/div/div/form/fieldset[13]/input")		

	
	firstname = "This field is required."
	alert_firstname = wait.until(EC.visibility_of_element_located((By.XPATH, str("/html/body/section/div[1]/div/div/form/fieldset[1]/p[1]/label[2]")))).text
	assert alert_firstname == firstname, "Mandatory field satisfied, should be blank for this test case."
	if alert_firstname == firstname:
		print("First Name mandatory alert is shown!")

	phonenumber = "This field is required."
	alert_phone = wait.until(EC.visibility_of_element_located((By.XPATH, str("/html/body/section/div[1]/div/div/form/fieldset[6]/label[2]")))).text
	assert alert_phone == phonenumber, "Mandatory field satisfied, should be blank for this test case."
	if alert_phone == phonenumber:
		print("Phone Number mandatory alert is shown!")

try:

	driver = webdriver.Chrome()
	driver.maximize_window()
	driver.get("https://www.way2automation.com/way2auto_jquery/registration.php#load_box")

	wait = WebDriverWait(driver, 10)
	positive_test()
	negative_test()

except Exception as e:
    # handle the exception here (print an error message, log the error, etc.)
    print("An error occurred:", e)

finally:
	driver.quit()




