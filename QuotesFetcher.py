import urllib3
import re
import datetime
import random
from bs4 import BeautifulSoup
import bs4

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()

url = 'https://www.goodreads.com/quotes/'
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

response = http.request('GET', url,headers=hdr,timeout=5)
soup = BeautifulSoup(response.data,features="html.parser")

result = soup.findAll('a', attrs={'href': re.compile("^/quotes/tag/")})

tag_list = []
cat_list=[]
quotes_list=[]
final_list=[]

for link in result:
    tag_list.append(str(link.get('href')).strip())
    cat_list.append(str(link.text).strip())
	
list(set(tag_list))
list(set(cat_list))



tag_name = random.choice(tag_list)
quotes_url = 'https://www.goodreads.com'+"/quotes/tag/love"
# print(quotes_url)
response = http.request('GET', url,headers=hdr,timeout=5)
soup = BeautifulSoup(response.data,features="html.parser")
result = soup.findAll('div', {"class":"quoteText"})

for link in result:	
	str =link.text
	soup = BeautifulSoup(str, "html.parser")
	# Removing CDATA
	if(soup.find(text=lambda tag: isinstance(tag, bs4.CData))):
		pass
	else:
		str = re.sub("[^\w'.!\s*]", "", str)
		str= re.sub("[\n\r]+", "", str)	
		quotes_list.append(str.strip("\n"))

print("-----Your Daily Quotes are here------")

for i,each in enumerate(quotes_list,start=1):
    print ("{}.{}\n".format(i,each))
    