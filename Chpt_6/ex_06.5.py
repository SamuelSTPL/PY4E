#Write code using find() and string slicing to extract the number at the end of the line below. 
#Convert the extracted value to a floating point number and print it out.

#Given text
text = "X-DSPAM-Confidence:    0.8475";

#Using the find() method 
start = text.find('0')
end = text.find('5')

#Slicing the required part
num = text[start: end + 1]

print(num)