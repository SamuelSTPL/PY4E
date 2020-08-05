#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
#Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for 
#all hours worked above 40 hours. 
#Put the logic to do the computation of pay in a function called computepay() 
#and use the function to do the computation. 
#The function should return a value. 
#Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
#You should use input to read a string and float() to convert the string to a number. 
#Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. 
#Do not name your variable sum or use the sum() function.

#Allow the use of exit()
import sys

#Check for input error (if not a numer)
try:
    hours = float(input('Enter hours: '))
    rate = float(input('Enter rate: '))

#Exit program if the input is not a number
except:
    print('Must be an integer')
    sys.exit()

#Function that will be called later on
def computepay(hours, rate):
    if hours > 40:
    #Calculate and print the actual pay
        overtime = (hours - 40) * (rate * 1.5)
        pay = (40 * rate) + overtime
        #Return the vale
        return pay
#Calling the function within the print statement with the inputs as arguments
print('Pay: ', computepay(hours, rate))
