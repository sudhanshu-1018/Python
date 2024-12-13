import requests
import json

query=input("what type of news you want to see?:")
url=f"https://newsapi.org/v2/everything?q={query}&from=2023-12-22&sortBy=publishedAt&apiKey=6459b2ee69b349b982d091fd309e4cfd"
r=requests.get(url)
# print(r.text)
news=json.loads(r.text)
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("------------------------------------------------------------------------------------")


