#imported libraries
import requests
import webbrowser
import time
from bs4 import BeautifulSoup

#declarations and list compilation
url="https://realpython.github.io/fake-jobs/"
page=requests.get(url)
soup=BeautifulSoup(page.content, "html.parser")
results=soup.find(id="ResultsContainer")
job_sects=results.find_all("div", class_="card-content")
job_locs=results.find_all("p", class_="location")
job_roles=results.find_all("h2", class_="title is-5")
python_jobs=results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
python_jobs_parents=[
    h2_element.parent.parent.parent for h2_element in python_jobs
]

#input script
user_choice=input("Would you like to display the url of each job or the role and location of each job? Type u for urls and r for roles and locations.")

#output script
if user_choice=="r":
    for job_loc in job_locs:
        for job_role in job_roles:
            print(job_loc, job_role, end="\n"*2)

elif user_choice=="u":
    for job_parent in python_jobs_parents:
        links=job_parent.find_all("a")
        for link in links:
            l_url=link["href"]
            print(f"Apply Here: {l_url}\n")

#script for invalid user_choice
else:
    print("You did not type u or r. Please run the script again")

url="https://www.microcenter.com/category/4294966937/graphics-cards?rd=1&vkw=gpu"
page=requests.get(url)
soup=BeautifulSoup(page.content, "html.parser")
results=soup.find(id="contentResults")
prod_sects=results.find_all("li", class_="product_wrapper")
high_ends=results.find_all(
    string=lambda text: "40" in text.lower()
)
prod_sects_parents=[
    li_element.parent.parent.parent.parent.parent.parent for li_element in prod_sects
]
high_ends_parents=[
    a_element.parent.parent.parent.parent.parent.parent for a_element in high_ends
]
skip_count=0

for job_parent in high_ends_parents:
    links=job_parent.find_all("a")
    for link in links:
        l_url=link["href"]
        if skip_count==0:
            webbrowser.open_new_tab(l_url)
            print(f"BUY HERE: {l_url}\n")
        if skip_count==4:
            skip_count=0
        else:
            skip_count=skip_count+1
        time.sleep(1.2)

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