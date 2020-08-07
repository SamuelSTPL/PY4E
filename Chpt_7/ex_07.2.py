#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values. 
#Do not use the sum() function or a variable named sum in your solution.

#Ask for file name
fname = input('Enter file name here: ')

#Lazyness
if len(fname) < 1 : fname = "mbox-short.txt"

#Open file with file handle
fhandle = open(fname)

#Initiating variables
count = 0
total = 0

#Seperate the whole text in lines
for line in fhandle:

    #Only keeping the one that we need
    if not line.startswith('X-DSPAM-Confidence:'):
        continue

    #Slicing the number
    start = line.find('0')
    number = float(line[start: ])
    
    #Calculating the sum
    count += 1
    total += number


print('Average spam confidence :', total / count)
    
    
