import requests
from bs4 import BeautifulSoup

url = "http://yellowpages.in/search/hyderabad/coffee"
response = requests.get(url)
html = response.contents

soup = BeautifulSoup(html)
#print soup.prettify()
data = soup.find_all("div",{"class":"eachPopular"})

for i in data:
	print i.contents[0].find_all("a",{"class":"eachPopularTitle hasOtherInfo"})[0].text
	print i.contents[1].find_all("a",{"class":"businessContact"})[0].text
	print i.contents[1].find_all("address",{"class":"businessArea"})[0].text
