#In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. 
#The program will use urllib to read the HTML from the data files below, 
#extract the href= vaues from the anchor tags, scan for a tag that is in a particular 
#position relative to the first name in the list, follow that link and repeat the process 
#a number of times and report the last name you find.

# http://py4e-data.dr-chuck.net/known_by_Mirabelle.html

#import urllib.request, urllib.parse, urllib.error
import urllib.request
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))

html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/known_by_Mirabelle.html''''url''', context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

lst = list()
for x in range(0,count):
    tags = soup('a')
    my_tags = tags[pos-1]
    needed_tag = my_tags.get('href', None)
    url = str(needed_tag)
    html = urllib.request.urlopen(url,context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    print(my_tags.get('href', None))