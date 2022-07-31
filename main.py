import bs4
import requests

# creating the request
res=requests.get("https://realpython.github.io/fake-jobs/")
print(type(res))



# Convert the request object to the Beautiful Soup Object  
soup=bs4.BeautifulSoup(res.content,'html.parser')

contents = soup.find_all("div",class_="card-content")

for content in contents:
    company = content.h3.text
    title = content.h2.text
    print(company, " - ", title)





