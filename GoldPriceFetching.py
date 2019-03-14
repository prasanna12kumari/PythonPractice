# Import Modules
import urllib3
import re
import datetime
from bs4 import BeautifulSoup


err_msg = "Some Error Occured. Please try later"

d = datetime. datetime.now()
tdate = d.strftime("%B %d, %Y")

city_code={'1':'Delhi',
	'1':'Hyderabad',
	'2':'Mumbai',
	'3':'Pune',
	'4':'Bangalore',
	'5':'Chennai',
	'6':'Madurai',
	'7':'Coimbatore',
	'8':'Kolkata',
	'9':'Lucknow',
	'10':'Ahmedabad',
	'11':'Patna'}	


def fetch_data(city_name):	
	try:
		urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
		http = urllib3.PoolManager()
		
		url = 'https://www.policybazaar.com/gold-rate-'+city_name +'/'
		hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
		
		response = http.request('GET', url,headers=hdr,timeout=5)
		soup = BeautifulSoup(response.data,features="html.parser")
		
		result = soup.findAll("div", {"class":"wd50 right"})
				
		if result is None or result == []:			
			result = "Data Not Available"
		return result
		
		
	except:
	
		return err_msg
		
def format_data():		
		
		
		city_no = input("Enter City code")
		
		while(int(city_no) > 11 or int(city_no) <=0):
			city_no = input("Please Enter Valid City code")
		
		city_name = city_code[city_no].lower()		
		result = fetch_data(city_name)
		extract_string_list=[]
		
		if result == "Data Not Available":
		
			print("Data Not Available")
			
		elif result == err_msg:
			
			print(err_msg)
		else:
			try:
				for i in result:
					extract_string_list.append(i.text)		
					
				pattern = re.compile("^\s*Rs.\s+([0-9]+)+.([0-9]*)$")

				pricelist = []
				
				for i in extract_string_list:	
					if pattern.match(i):
						pricelist.append(i)
						
				if len(pricelist)== 2:	
				
					print("\n"+city_name +" "+ tdate)
					print("_________________________")
					print("\n22 Carat Gold Rate is " + pricelist[0])
					print("24 Carat Gold Rate is " + pricelist[1])
					
				else:
					print(err_msg)
			except:
				print(err_msg)
				
		
			
		

		
format_data()

