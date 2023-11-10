#download the libraries
# pip install pyshorteners
# pip install pyperclip
#import the pyshorteners library 
import pyshorteners
#Create a variable URL to take the input from user
URL = input("Enter the URL : ")
#using funtions define a function to shorten the URL
def shortenURL(URL):
    #create an object to shorten teh URL
    S = pyshorteners.Shortener()
    #print the shortened URL
    print("Your shortened URL is : ", S.tinyurl.short(URL))
#call the function
shortenURL(URL)
