#imported libraries
import cloudscraper
from bs4 import BeautifulSoup

query=input("input query keyword")
scraper=cloudscraper.create_scraper()
url="https://www.indeed.com/jobs?q=&l=Philadelphia%2C+PA&from=searchOnHP&vjk=064a3e17be20ac8b"
page=scraper.get(url)
soup=BeautifulSoup(page.content, "html.parser")
results=soup.find("div", id="jobsearch-Main")

print(results.prettify())