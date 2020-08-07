#Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line 
#(i.e. the entire address of the person who sent the message). 
#Then print out a count at the end.

#Ask the user for file name
fname = input('Enter file name: ')

#Lazyness
if len(fname) < 1 : fname = 'mbox-short.txt'

#Open file
fhandle = open(fname)

#Initiate the variable
count = 0

#Seperate the text in lines
for line in fhandle:

    #Take off the blanks ont the right side
    line.rstrip()
    #Splite the line in words
    words = line.split()

    #Guardian 
    if len(words) < 3 or words[0] != 'From': continue

    print(words[1])

    count += 1

print("There were", count, "lines in the file with From as the first word")