#importing the random library
import random
#Creating a variable which contains all the charecters
charecters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
#Creating a variable to define the length of the password
length = int(input("Enter password length : "))
password = ""
#Using for loop to use charecters randomly 
for a in range(length):
    password += random.choice(charecters)
#printing the password    
print(password)