from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
url="https://appbrewery.github.io/Zillow-Clone/"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response=requests.get(url=url,headers=header)
data=response.text
soup=BeautifulSoup(data,"html.parser")
all_link_elements = soup.select(".StyledPropertyCardDataWrapper a") 
# Python list comprehension 
all_links = [link["href"] for link in all_link_elements] 
print(f"There are {len(all_links)} links to individual listings in total: \n")
print(all_links)
all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
all_address = [address.get_text().replace("|","").strip() for address in all_address_elements ]
print(f"There are {len(all_address)} address to individual listings in total: \n")

print(all_address)
all_price_element= soup.select(".PropertyCardWrapper span")
all_price=[price.get_text().replace("/mo", "").split("+")[0] for price in all_price_element if "$" in price.text]
print(all_price)

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
GOOGLE_LINK = os.environ.get("GOOGLE_LINK")
for n in range (len(all_links)):
    driver.get(GOOGLE_LINK)
    time.sleep(2)
    address=driver.find_element(by=By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price=driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link=driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit=driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    address.send_keys(all_address[n])
    price.send_keys(all_price[n])
    link.send_keys(all_links[n])
    submit.click()
    

