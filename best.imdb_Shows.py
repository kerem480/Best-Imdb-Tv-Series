import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/list/ls038130473/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="main")

job_elements=results.find_all("div",class_="lister-item-content")

for job_element in job_elements:
    title_element=job_element.find("h3",class_="lister-item-header").text
    star_element=job_element.find("p",class_="text-muted text-small").text


    print(title_element.strip()+star_element.strip() + "\n"+"**************************")



