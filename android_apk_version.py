# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from bs4 import BeautifulSoup 
import csv
import requests
import pandas as pd
r=requests.get("https://www.androidapksfree.com/devapk/opera-software-asa/opera-mini/")
soup=BeautifulSoup(r.content)
data=soup.find_all("div",{"class":'app-more-info-schema'})
records=[]
rel=soup.select('div > div > div > div > span')
rd=[]

for res in data:
	version=res.find('span').text
	file_size=res.contents[3].text[0:19].strip()
	andriod=res.contents[3].text[19:42].strip()
	records.append((version,file_size,andriod))
	
for i in rel:
	r_date=i.text
	rd.append((r_date))
	


df=pd.DataFrame(records,rd,columns=['version','file_size','andriod'])


df.to_csv('opera_mini.csv', index=False, encoding='utf-8')
df=pd.read_csv('opera_mini.csv')
df['date']=rd
df.to_csv('opera_mini.csv')


