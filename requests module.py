import requests
response=requests.get("https://www.hotstar.com")
print(response.text)

# post requests
import requests
url="https://jsonplaceholder.typicode.com/posts"
data={
    "title":'harry',
    "body":'bhai',
    "user Id":12
}
headers={
    'content-type':'application/json; charset=UTF-8',
}
response=requests.post(url,headers=headers,json=data)
print(response.text)


# bs4 module (beautiful soup)
import requests
from bs4 import BeautifulSoup
url="https://www.hotstar.com"

r=requests.get(url)
# print(r.text)

soup=BeautifulSoup(r.text,'html.parser')
# print(soup.prettify)
for heading in soup.find_all("head"):
    print(heading.text)
