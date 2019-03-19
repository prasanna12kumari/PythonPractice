import urllib3
import re
import datetime
from bs4 import BeautifulSoup
import bs4


def fetch_category_links(url,hdr,http):
	response = http.request('GET', url,headers=hdr,timeout=5)
	soup = BeautifulSoup(response.data,features="html.parser")
	result = soup.findAll('a', attrs={'href': re.compile("^/genres/")})	
	category_links=[]
	category_names=[]
	for link in result:
		category_links.append(str(link.get('href')).strip())	
		category_names.append(str(link.text).strip())	
	return category_links,category_names
	
	
def fetch_book_links(url,hdr,http):
	response = http.request('GET', url,headers=hdr,timeout=5)
	soup = BeautifulSoup(response.data,features="html.parser")

	result = soup.findAll('a', attrs={'href': re.compile("^/book/show/")})
	books_url = []
	for link in result:
		books_url.append(str(link.get('href')).strip())		

	return books_url
	

def fetch_book_ratings(url,hdr,http):
	response = http.request('GET', url,headers=hdr,timeout=5)
	soup = BeautifulSoup(response.data,features="html.parser")

	
	book_rating = soup.find('span', {"itemprop":"ratingValue"})	

	book_name = soup.find('title')	
	book_dict={}
	book_dict.update({book_name.text:str(book_rating.text).strip('\n')})	
	return book_dict

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()	


url = "https://www.goodreads.com/"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

category_links,category_names = fetch_category_links(url,hdr,http)
f = open('BookRatings.txt', 'w')
count = 0
for i in category_links:
	f.write("%s Books Ratings\n\n"%category_names[count])
	f.write
	home_url = "https://www.goodreads.com"+str(i)
	book_links = fetch_book_links(home_url,hdr,http)
	result=[]
	count = count + 1
		book_url = "https://www.goodreads.com"+str(i)
		result.append(fetch_book_ratings(book_url,hdr,http))
	for i in result:
		for j in i:				
			f.writelines(str(j)+" : "+str(i[j]))		
			f.writelines("\n")
	f.write("\n")
	
	
	