#Write a program to read through the mbox-short.txt and figure out the distribution by hour 
#of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time
#and then splitting the string a second time using a colon.

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

#Once you have accumulated the counts for each hour, print out the counts, sorted by hour.


import sys

#Ask for filename
fname = input('Enter file name here: ')

#Lazyness
if len(fname) < 1 : fname = 'mbox-short.txt'

#Check for file error
try:
    fhandle = open(fname)

except:
    print('File name invalid')
    sys.exit(1)

#Initiate dict
timelist = {}

#Split the text in lines, then in words
for line in fhandle:
    line.rstrip()

    words = line.split()

    #Guardian
    if len(words) < 3 or words[0] != 'From':
        continue
    
    #Not necessay, but easier to understand
    time = words[5]
    
    #Double split
    hours = time.split(':')

    #Isolate the hour
    hour = hours[0]

    #Add hour and values to the dict
    timelist[hour] = timelist.get(hour, 0) + 1

    #Iterate in dict, create a list of tuples, then sort them
    lst = sorted([(k,v) for k,v in timelist.items()])

#Print it so it looks prettier    
for k,v in lst:
    print(k,v)