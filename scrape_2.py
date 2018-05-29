

from bs4 import BeautifulSoup 
import requests
r=requests.get("http://www.padasalai.net/2017/09/latest-11th-study-materials-physics.html?m=1")

soup = BeautifulSoup(r.content)

data=soup.select('tr > td + td > p > span > a')

#new_data=soup.select('tr > td > p > span > a')

#data=soup.select('tr  td  p  span a')

#for i in new_data:

for i in data:
	
	print i.text
	print i.get('href')
	print("\n")	\

'''

from bs4 import BeautifulSoup 
import urllib2
r=urllib2.urlopen("https://lagunita.stanford.edu/courses").read()
soup=BeautifulSoup(r)


data= soup.select("article > a")

new=soup.find_all("div",{"class":"course-date"})


for i in data:
	print i.text.strip()
	print i.get('href')

for j in new:
	str1=("Starts: ")
	t=j.get("data-datetime")
	str2=(t[0:10])
	d=str1+str2
	print(d)
	'''


