from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#keep chrome browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver= webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
stats = driver.find_elements(By.XPATH, value = '//*[@id="articlecount"]/ul/li[2]/a[1]')

search = driver.find_elements(By.XPATH, value='//*[@id="searchform"]/div/div/div[1]/input')

search.send_keys("Python" , Keys.ENTER)
