from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep



# create a new Chrome browser instance
service = Service(executable_path=r'C:\Users\white\Downloads\internship-project\internship-project-1\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the urlclear
driver.get('https://www.google.com/')

# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('table')

# wait for 4 sec
sleep(4)

# click search button
driver.find_element(By.NAME, 'btnK').click()

# verify search results
assert 'table' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
