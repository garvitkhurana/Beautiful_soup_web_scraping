import nltk
from bs4 import BeautifulSoup 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import requests
punc=[]
url=input("Enter the website: ")
r=requests.get(url)
soup=BeautifulSoup(r.text)
text = soup.get_text(strip=True)
tokens=[t for t in text.split() ]
stop_words=stopwords.words('english')
s=input("Enter stop words: ")
new_stop_words=s.split()
new_stop_words=stop_words+new_stop_words
for i in range(0,len(string.punctuation)):
    punc.append(string.punctuation[i])
stop_words_with_punctuation=new_stop_words+punc
clean_tokens=[t for t in tokens if t not in stop_words_with_punctuation]
key=input("Enter the word to be found: ")
if(key not in clean_tokens):
    print("Word not found\n")
else:
    print("The word {} is found at {}".format(key,clean_tokens.index(key)))