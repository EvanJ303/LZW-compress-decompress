#imported libraries
import webbrowser
import requests
import time
from bs4 import BeautifulSoup

url="https://www.microcenter.com/category/4294966937/graphics-cards?rd=1&vkw=gpu"
page=requests.get(url)
soup=BeautifulSoup(page.content, "html.parser")
results=soup.find(id="contentResults")
prod_sects=results.find_all("li", class_="product_wrapper")
high_ends=results.find_all(
    string=lambda text: "4060" in text.lower()
)
prod_sects_parents=[
    li_element.parent.parent.parent.parent.parent for li_element in prod_sects
]
high_ends_parents=[
    a_element.parent.parent.parent.parent.parent for a_element in high_ends
]
skip_count=0

for high_end_parent in high_ends_parents:
    links=high_end_parent.find_all("a")
    for link in links:
        l_url=link["href"]
        if skip_count==0:
            #webbrowser.open_new_tab(l_url)
            print(f"BUY HERE: {l_url}\n")
        if skip_count==4:
            skip_count=0
        else:
            skip_count=skip_count+1
        #time.sleep(0.1)