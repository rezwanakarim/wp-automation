from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import time

load_dotenv()

WP_USERNAME = os.getenv("WP_USERNAME")
WP_PASSWORD = os.getenv("WP_PASSWORD")

PATH = os.getenv("CHROMEDRIVER_PATH") 
service = Service(PATH)
driver = webdriver.Chrome(service=service)

driver.get("http://wppool.test/wp-admin") 

username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user_login")))
password = driver.find_element(By.ID, "user_pass")
login_button = driver.find_element(By.ID, "wp-submit")

username.send_keys(WP_USERNAME)
password.send_keys(WP_PASSWORD)
login_button.click()


WebDriverWait(driver, 10).until(EC.url_contains("wp-admin"))

driver.get("http://wppool.test/wp-admin/plugins.php")

try:
    wp_dark_mode = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "WP Dark Mode")))
    print("WP Dark Mode is installed.")
except:
    print("WP Dark Mode is not installed.")
    driver.quit()
    exit()


driver.get("http://wppool.test/wp-admin/admin.php?page=wp-dark-mode#/admin")

# Locate and enable Admin Dashboard Dark Mode
try:

    admin_dark_mode_toggle = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/div/div/div/div[2]/div[2]/section[1]/div[1]/div[1]/label/div[1]/div"))
    )

    if not admin_dark_mode_toggle.is_selected():
        admin_dark_mode_toggle.click()
       
        save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/div/div/div/div[2]/div[3]/button[2]")))
        driver.execute_script("arguments[0].scrollIntoView(true);", save_button)
        save_button.click()
        print("Admin Dashboard Dark Mode enabled.")

        # Validate if Dark Mode is applied
        dark_mode_validate = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/ul[1]/li[7]/div/div/div/span[2]"))
        )
        
        if dark_mode_validate:
            print("Dark Mode is successfully applied to the Admin Dashboard.")
        else:
            print("Dark Mode is not applied. Please check the settings.")
    
    else:
        print("Admin Dashboard Dark Mode is already enabled.")

except Exception as e:
    print(f"Could not enable Admin Dashboard Dark Mode or validate. Error: {e}")



driver.get("http://wppool.test/wp-admin/admin.php?page=wp-dark-mode#/switch")

#Change Floating Switch Style
try:
    specific_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/div/div/div/div[2]/div[2]/div/section/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[3]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", specific_option)
    specific_option.click()

    save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/div/div/div/div[2]/div[3]/button[2]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", save_button)
    save_button.click()
    print("Floating Switch Style changed to the specific option and settings saved.")

except Exception as e:
    print(f"Could not change floating switch style. Error: {e}")


# Change Floating Switch Size
try:
    custom_option = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/div/div/div/div[2]/div[2]/div/section/div[2]/div/div[2]/div[4]/div/div[1]/div[1]/div[2]/div[6]"))
    )
    custom_option.click()

    switch_size_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/div/div/div/div[2]/div[2]/div/section/div[2]/div/div[2]/div[4]/div/div[1]/div[1]/div[3]/div[2]/div/div[2]/input"))
    )
    switch_size_input.clear()
    switch_size_input.send_keys("220")

    save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/div/div/div/div[2]/div[3]/button[2]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", save_button)
    save_button.click()
    print("Custom Switch Size scaled to 220 and settings saved.")

except Exception as e:
    print(f"Could not customize button Error: {e}")

# Change Floating Switch Position to Left
try:
    floating_switch_position = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/div/div/div/div[2]/div[2]/div/section/div[2]/div/div[2]/div[4]/div/div[1]/div[2]/div[2]/div[1]"))
    )
    floating_switch_position.click()

    save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/div/div/div/div[2]/div[3]/button[2]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", save_button)
    save_button.click()
    print("Floating Switch Position changed to left.")

except Exception as e:
    print(f"Could not change Floating Switch Position. Error: {e}")


driver.get("http://wppool.test/wp-admin/admin.php?page=wp-dark-mode#/accessibility")

#Disable Keyboard Shortcut
try:
    keyboard_shortcut_toggle = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/div/div/div/div[2]/div[2]/div/div[6]/div[1]/label/div[1]/div/span"))
    )
    if keyboard_shortcut_toggle.is_selected():
        keyboard_shortcut_toggle.click()

    save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/div/div/div/div[2]/div[3]/button[2]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", save_button)
    save_button.click()
    print("Keyboard Shortcut disabled and settings saved.")

except Exception as e:
    print(f"Could not disable Keyboard Shortcut. Error: {e}")


driver.get("http://wppool.test/wp-admin/admin.php?page=wp-dark-mode#/animation")

# Enable Page Transition Animation and Change Effect
try:
    page_transition_toggle = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/div/div/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div/label/div[1]/div"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", page_transition_toggle)

    animation_effect = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/div/div/div/div[2]/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/span[1]"))
    )
    animation_effect.click()

    save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/div/div/div/div[2]/div[3]/button[2]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", save_button)
    save_button.click()
    print("Page Transition Animation enabled and effect changed.")

except Exception as e:
    print(f"Could not enable Page Transition Animation. Error: {e}")

# Frontend Dark mode Validation
try:
    driver.get("http://wppool.test/")
    frontend_dark_mode_validate = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div/div[1]"))
    )
    if frontend_dark_mode_validate:
        print("Dark Mode is successfully applied frontend.")
    else:
        print("Dark Mode is not applied in frontend.")
except Exception as e:
    print(f"Could not validate Dark Mode in frontend. Error: {e}")

driver.quit()
