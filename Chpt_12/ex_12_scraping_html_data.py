#Scraping Numbers from HTML using BeautifulSoup In this assignment you will write 
#a Python program similar to http://www.py4e.com/code3/urllink2.py. 
#The program will use urllib to read the HTML from the data files below, and parse the data, 
#extracting numbers and compute the sum of the numbers in the file.

# http://py4e-data.dr-chuck.net/comments_850873.html

#Importing libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

#Initiate the list variable
numbers = list()

# Retrieve all of the span tags
tags = soup('span')

#Loop then add all numbers on the web page to the list 
for tag in tags:
    numbers.append(int(tag.contents[0]))
    
print(sum(numbers))
