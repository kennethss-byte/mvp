from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import time

def slider_test():
	# Locate slider element
	slider = wait.until(EC.visibility_of_element_located((By.ID, "fluency")))
	time.sleep(2)

	# Move the pointer of the slider
	actions = ActionChains(driver)
	# In this case, since min value is 0 and max value is 5, each value has offset 20. We set offset value as 80 to change the value to 4
	actions.move_to_element(slider).drag_and_drop_by_offset(slider, 80, 0).perform()

	# Get the new slider value
	slider_value = int(wait.until(EC.visibility_of_element_located((By.ID, "fluency_validate"))).text)

	# Verify the result
	expected_value = 4
	assert slider_value == expected_value, f"Slider value: {slider_value} did not match expected value: {expected_value}"
	if slider_value == expected_value:
		print(f"Slider value matched!")

def menu_select_test():
	# Locate select menu
	select_element = wait.until(EC.visibility_of_element_located((By.ID, "select_lang")))
	time.sleep(2)

	# create select object
	select = Select(select_element)
	time.sleep(2)

	# select option by value
	select.select_by_value("python")
	time.sleep(2)

	# verify selected option
	expected_value = "python"
	# selected_option = select.first_selected_option.text
	selected_value = wait.until(EC.visibility_of_element_located((By.ID, "select_lang_validate"))).text
	assert selected_value == expected_value, f"Selected value: {selected_value} did not match expected value: {expected_value}"
	if selected_value == expected_value:
		print(f"Selected value in select menu matched!")


def read_only_textbox_test():
	# Locate read only textbox
	read_only_textbox = wait.until(EC.visibility_of_element_located((By.ID, "common_sense")))

	# get the readonly attribute value
	read_only_attr_value = read_only_textbox.get_attribute("readonly")

	# assert the read-only attribute value
	assert read_only_attr_value == "true", "Mandatory Skill (Read-Only textbox) is not read-only"
	if read_only_attr_value:
		print("Mandatory Skill (Read-Only textbox) is read-only!")


def upload_file():
	# DEFINE YOUR LOCAL PATH HERE! <local_path>/mvp/Dummy/xxx.png
	first_pic_filepath = "/Users/kennethsarashadi/Downloads/mvp/Dummy/cici.png"
	second_pic_filepath = "/Users/kennethsarashadi/Downloads/mvp/Dummy/cici2.png"
	
	upload_file_1 = wait.until(EC.visibility_of_element_located((By.ID, "upload_cv")))
	upload_file_1.send_keys(first_pic_filepath)

	expected_upload = "cici.png"
	uploaded_file = wait.until(EC.visibility_of_element_located((By.ID, "validate_cv"))).text
	assert uploaded_file == expected_upload, "Uploaded file name is not matched"
	if uploaded_file == expected_upload:
		print("File is correctly attached!")

	upload_file_2 = wait.until(EC.visibility_of_element_located((By.ID, "upload_files")))
	upload_file_2.send_keys(f"{first_pic_filepath}\n{second_pic_filepath}")

	expected_uploads = "cici.png cici2.png"
	uploaded_files = wait.until(EC.visibility_of_element_located((By.ID, "validate_files"))).text
	# print(uploaded_files)
	assert uploaded_files == expected_uploads, "Uploaded file names are not matched"
	if uploaded_files == expected_uploads:
		print("Files are correctly attached!")

	time.sleep(5)

try:
	# Create a new instance of a Chrome driver
	driver = webdriver.Chrome()
	driver.maximize_window()

	# Navigate to the URL
	driver.get("https://dineshvelhal.github.io/testautomation-playground/forms.html")

	wait = WebDriverWait(driver, 10)
	slider_test()
	menu_select_test()
	read_only_textbox_test()
	upload_file()

	time.sleep(5)

except Exception as e:
    # handle the exception here (print an error message, log the error, etc.)
    print("An error occurred:", e)

finally:
    print("----- ALL TESTS ARE PASSED! -----")
	driver.quit()







