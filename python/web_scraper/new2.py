import requests
from bs4 import BeautifulSoup

url = "https://www.microcenter.com/category/4294966937/graphics-cards?rd=1&vkw=gpu"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="contentResults")
prod_sects = results.find_all("li", class_="product_wrapper")

for section in prod_sects:
    links = section.find_all("a", href=True)
    for link in links:
        # Extract the card name based on actual HTML structure
        card_name = link.find("h2").text.strip()  # Adjust this based on the real structure
        # Check if the card name indicates a high-end card
        if "40" in card_name.lower():  # Adjust this condition based on actual card names
            card_url = link["href"]  # Get the URL from the href attribute
            print(f"Buy Here: {card_url}\n")