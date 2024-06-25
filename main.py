import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

google_forms_link = "https://docs.google.com/forms/d/e/1FAIpQLSfQZOv8d3v7wl6YuJ1y3E1sqYEZFDtWrTgc7uaZP2PTONxTeQ/viewform"
rentals_url = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(rentals_url)
soup = BeautifulSoup(response.content, "html.parser")


listings_group = soup.find("ul", class_="List-c11n-8-84-3-photo-cards")

listings = soup.find_all('a', {'data-test': 'property-card-link'})

listings_prices = soup.find_all("span", {'data-test': 'property-card-price'})

#list of addresses
addresses = listings_group.find_all("address")

list_of_addresses = [address.get_text(strip=True) for address in addresses]


#list of links
list_of_links = []
for link in listings:
    url = link["href"]
    list_of_links.append(url)


#list of prices
list_of_prices = []
for listings_price in listings_prices:
    price_text = listings_price.get_text()
    stripped_price = price_text.replace("+/mo", "").replace("/mo", "").replace("+ 1bd", "").strip()
    list_of_prices.append(stripped_price)

#SELENIUM AUTOFILL
driver = webdriver.Chrome()
driver.get(google_forms_link)

def input_address():
    address_input = driver.find_element(By.XPATH,
                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(list_of_addresses[i])

def input_price():
    price_input = driver.find_element(By.XPATH,
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(list_of_prices[i])

def input_link():
    link_input = driver.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(list_of_links[i])

def submit():
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit_button.click()

def submit_another():
    submit_another_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit_another_button.click()


for i in range(len(list_of_prices)):
    time.sleep(5)
    input_address()
    input_price()
    input_link()
    submit()
    time.sleep(3)
    submit_another()





