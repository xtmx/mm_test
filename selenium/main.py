
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd

# Settings
RETRY_TIMES = 3
WAIT_TIME = 3
START_URL = "https://www.montmere.com/test.php"

# Credentials (shouldn't be here)
user = 'test'
passwd = 'test'

# Set Selenium driver
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

for T in range(0, RETRY_TIMES):
    # Call URL
    driver.get(START_URL)

    # Wait to load, check/retry.
    wait_id = 'username'
    try:
        WebDriverWait(driver, WAIT_TIME).until(EC.presence_of_element_located((By.ID, wait_id)))
    except:
        continue

    # Login
    username = driver.find_element_by_id("username").send_keys(user)
    password = driver.find_element_by_id("password").send_keys(passwd)
    driver.find_element_by_xpath("//input[@type='submit' and @value='Login']").click()

    # Wait to load, check/retry.
    the_table_xpath = "//table[contains(//tr/th/text(), 'Make')]"
    try:
        WebDriverWait(driver, WAIT_TIME).until(EC.presence_of_element_located((By.XPATH, the_table_xpath)))
    except:
        continue

    # Get data
    table = driver.find_element(By.XPATH, the_table_xpath)
    rows = table.find_elements(By.XPATH, './tr')

    arr = []
    for row in rows:
        cells = [c.text for c in row.find_elements(By.XPATH, './td')]
        if cells:
            arr.append(cells)

    # Stop retrying
    if arr:
        break
        

if arr:
    # Format data
    df = pd.DataFrame(arr, columns=['makes', 'models', 'years'])

    # Output to csv
    df.to_csv('output.csv')


# Quit Selenium driver
driver.quit()