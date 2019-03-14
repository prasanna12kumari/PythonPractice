# Import Modules
import urllib3
import re
import datetime
from bs4 import BeautifulSoup


err_msg = "Some Error Occured. Please try later"

d = datetime.datetime.now()
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

print("Welcome to Gold Price Today Application")
print("\n City List with their codes\n")
for k in city_code:
	print(city_code[k]+" : "+ k)
	

def fetch_data(city_name):	
	''' Getting gold price from the website'''
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
		
		''' Fetch the Gold Price and format'''
		
		city_no = input("Enter City code")
		
		while(int(city_no) > 11 or int(city_no) <=0):
			city_no = input("Please Enter Valid City code")
		
		city_name = city_code[city_no].lower()		
		result = fetch_data(city_name)
		extract_string_list=[]
		
		if result == "Data Not Available":
		
			return("Data Not Available")
			
		elif result == err_msg:
			
			return(err_msg)
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
					print("\n"+city_name.capitalize() +" "+ tdate)
					print("_________________________")
					print("\n22 Carat Gold Rate is " + pricelist[0])
					print("\n24 Carat Gold Rate is " + pricelist[1])
					print("\nYou can also be provided with the pdf for the same!!!")
					linelist = []
					linelist.append(city_name.capitalize() +" "+ tdate)
					linelist.append("22 Carat Gold Rate is " + pricelist[0])
					linelist.append("24 Carat Gold Rate is " + pricelist[1])
					return linelist
					
				else:
					return(err_msg)
			except:
				return(err_msg)
	
def pdf_gen():
	''' PDF Generation '''
	from fpdf import FPDF
	 
	content = format_data()
	if isinstance(content, list):
		pdf = FPDF()
		pdf.add_page()
		pdf.set_font("Arial", size=12)
		pdf.set_text_color(41, 128, 185)
		pdf.cell(200, 10, txt = "Gold Price Today", ln = 1, align = "C")
		pdf.line(50, 20, 160, 20)
		pdf.set_line_width(2)
		pdf.set_draw_color(54,69,79)
		pdf.set_text_color(211, 84, 0)
		
		pdf.cell(0, 10, txt = content[0], ln = 33, align = "L")
		pdf.set_text_color(39, 174, 96)
		pdf.cell(0, 10, txt = content[1], ln = 34, align = "L")
		pdf.cell(0, 10, txt = content[2], ln = 35, align = "L")
		pdf.image("Gold.jpg", x = 110, y = 30,w = 50,h=50)
		date_time =  datetime.datetime.now().strftime("%Y%m%d__%H%M%S")		
		pdf.output("GoldPriceToday__"+str(date_time)+".pdf")
	else:
		print(content)

pdf_gen()

import sys
confirm_exit = input("\nPress enter you exit")

if confirm_exit == "":
	sys.exit()
else:	
	sys.exit()

#code for converting this into exe

### pyinstaller --onefile <your_script_name>.py
### pyinstaller --onefile GoldPriceFetching.py