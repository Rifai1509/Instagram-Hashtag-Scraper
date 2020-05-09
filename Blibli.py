import requests
from bs4 import BeautifulSoup

url = 'https://www.blibli.com/jual/iphone?page=1&start=0&searchTerm=iphone&intent=true&merchantSearch=true&multiCategory=true&customUrl=iphone&sort=0&category=IP-1000001'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
print(soup)
