#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times
#they appear in the file. 
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

#Allow exit()
import sys

#Ask filename
fname = input('Enter file name here: ')

#Lazyness
if len(fname) < 1 : fname = 'mbox-short.txt'

#Initiate the dict
senders = {}

#Check for file error
try:
    fhandle = open(fname)

except:
    print('File name invalid')
    sys.exit(1)

#Split line, then words from text
for line in fhandle:
    line.rstrip()
    words = line.split()
    
    #Guardian
    if len(words) < 3 or words[0] != 'From':
        continue

    #Not necessary, but makes it easier to comprehend
    email = words[1]

    #Add emails and or change their values in the dict
    senders[email] = senders.get(email, 0) + 1

#Initiate variables
bigname = None
bigcount = None

#Looping inside the dict to find the biggest count
for name, count in senders.items():
    if bigcount is None or count > bigcount:
        bigname = name
        bigcount = count

print(bigname, bigcount)
    
    
