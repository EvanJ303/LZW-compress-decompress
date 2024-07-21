#imported libraries
import cloudscraper
from bs4 import BeautifulSoup
import time

query=input("input query keyword")
state=input("input state")
scraper=cloudscraper.create_scraper()
base_url="https://www.indeed.com/jobs"

url_params={
    "q":query,
    "l":state,
    "from":"searchOnDesktopSerp"
}

url=base_url + "?" + "&".join(f"{k}={v}" for k, v in url_params.items())
page=scraper.get(url)
time.sleep(5)
soup=BeautifulSoup(page.content, "html.parser")
results=soup.find("div", id="jobsearch-Main")
job_sects=results.find_all("table", role="presentation")
job_locs=[]

for job_sect in job_sects:
    div_elems=job_sect.find_all("div")

    for div_elem in div_elems:
        content=div_elem.get_text(strip=True)
        if f", {state}" in content:
                job_locs.append(content)

print(job_locs)