import requests
from bs4 import BeautifulSoup

google_forms_link = "https://docs.google.com/forms/d/e/1FAIpQLSfQZOv8d3v7wl6YuJ1y3E1sqYEZFDtWrTgc7uaZP2PTONxTeQ/viewform?usp=sf_link"
rentals_url = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(rentals_url)
soup = BeautifulSoup(response.content, "html.parser")


listings_group = soup.find("ul", class_="List-c11n-8-84-3-photo-cards")

listings = soup.find_all('a', {'data-test': 'property-card-link'})

listings_prices = soup.find_all("span", {'data-test': 'property-card-price'})

#list of addresses
addresses = listings_group.find_all("address")

list_of_addresses = [address.get_text(strip=True) for address in addresses]

print(list_of_addresses)

#list of links
list_of_links = []
for link in listings:
    url = link["href"]
    list_of_links.append(url)

print(list_of_links)

#list of prices
list_of_prices = []
for listings_price in listings_prices:
    list_of_prices.append(listings_price.get_text())

print(list_of_prices)