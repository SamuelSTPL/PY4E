import re

#Ask for file file
fname = input('Enter file name: ')
if len(fname) < 1 : fname = "regex_sum_850871.txt"

#Check for file errors
try:
    #Open file
    fhandle = open(fname)

except:
    #Quit program if error
    print("Could not open file")
    quit

#Initiate list and variable
numlist = list()
sum = 0

#Divide the text by line, then check for every integer. Then adds everything to the list
for line in fhandle:
    number = re.findall('[0-9]+',line)
    numlist = numlist + number

#Calculate the sum of each number in the list
for num in numlist:
    sum = sum + int(num)

print(sum)