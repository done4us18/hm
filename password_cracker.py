# module

import os,sys,time,random
from random import *

os.system("clear")

# main
guess=""
password=input("Enter Password > ")
wordlist = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
while(guess in password):
    Guess=""
    for letter in password:
        guessletter=wordlist[randint(0,25)]
        guess=str(guessletter) + str(guess)
    print("Password Cracked >",guess)
print("Congratulations now you have become a Pro Hacker")
