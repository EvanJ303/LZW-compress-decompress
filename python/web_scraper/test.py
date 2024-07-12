#imported libraries
import requests
from bs4 import BeautifulSoup

#declarations and list compilation
url="https://realpython.github.io/fake-jobs/"
page=requests.get(url)
soup=BeautifulSoup(page.content, "html.parser")
results=soup.find(id="ResultsContainer")
print(results)