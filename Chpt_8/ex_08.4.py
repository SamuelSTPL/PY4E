#Open the file romeo.txt and read it line by line. 
#For each line, split the line into a list of words using the split() method. 
#The program should build a list of words. 
#For each word on each line check to see if the word is already in the list and if not append it to the list. 
#When the program completes, sort and print the resulting words in alphabetical order.

#Ask the user for filename
fname = input('Enter file name: ')

#Lazyness
if len(fname) < 1 : fname = 'romeo.txt'

#Open file
fhandle = open(fname)

#Initiate an empty list
lst = list()

#Seperate each line in text
for line in fhandle:

    #Seperate each word in each line
    for word in line.split():
        
        #Append word in the list
        if word not in lst:
            lst.append(word)

#Sort and print the list
lst.sort()
print(lst)
