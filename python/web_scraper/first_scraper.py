#imported libraries
import requests
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