from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import random

# Setup Chrome WebDriver (Ensure chromedriver.exe matches your Chrome version)
chromedriver_path = "chromedriver.exe"  # Update if needed
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # Helps bypass bot detection

# Initialize Chrome WebDriver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

def check_tiktok_email(email):
    """Function to Check if Email is Registered on TikTok Business"""
    driver.get("https://business.tiktok.com/login")
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    try:
        # Locate email input field and enter email
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_input.send_keys(email)
        
        # Locate password field and enter dummy password
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_input.send_keys("Spiderman123456#")
        
        # Locate and click login button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "TikTok_Ads_SSO_Login_Btn_new"))
        )
        login_button.click()
        
        time.sleep(10)  # Delay for potential CAPTCHA prompt
        input("Solve CAPTCHA manually in browser, then press Enter to continue...")
        time.sleep(5)  # Additional wait time
        
        # Check for error messages based on provided HTML structure
        error_elements = driver.find_elements(By.XPATH, '//div[contains(@class, "login-error-tip")]/div[@class="content-wrapper"]/div[contains(text(), "We couldn\'t find an account with that email.")]')
        
        if error_elements:
            return f"{email}:  Not Registered  :  Available"
        else:
            return f"{email}:  Registered  :  Unavailable"
    except Exception as e:
        return f"{email}:  Error - {str(e)}"

# Load Emails from CSV (Ensure 'emails.csv' exists and has an 'email' column)
try:
    df = pd.read_csv("emails.csv")
    email_list = df["email"].tolist()
except FileNotFoundError:
    print("❌ Error: 'emails.csv' not found. Please check the file path and try again.")
    driver.quit()
    exit()

# Check Each Email and Store Results
results = []
for email in email_list:
    result = check_tiktok_email(email)
    print(result)
    results.append(result)
    
    # 🔴 Random delay to avoid detection
    wait_time = random.uniform(5, 10)  # Random wait between 5-10 seconds
    print(f"Waiting {round(wait_time, 2)} seconds before checking the next email...")
    time.sleep(wait_time)

# Save results to CSV
results_df = pd.DataFrame(results, columns=["Result"])
results_df.to_csv("results.csv", index=False)

# Close browser driver
print(" Process completed. Check 'results.csv' for output.")
driver.quit()
