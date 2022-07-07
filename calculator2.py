# modules
import os,sys,time


# yes or no
def again():
    a = input("Do you want to continue..? [y/n] ~+> ")
    if a =="y" or a =="Y":
        os.system("python calculator2.py")
    elif a =="n" or a =="N":
        print ("Thank you for using this calculator.")
        time.sleep(0.8)
        print ("Dont'n forget to subscribe my channel")
        time.sleep(0.8)
        sys.exit()
    else:
        print ("wrong input")
        time.sleep(0.8)
        print ("Enter the correct input")
        time.sleep(0.8)
        again()
# input length, width, height
os.system("clear")
length = int(input("Enter the length : "))
width = int(input("Enter the width   : "))
height = int(input("Enter the height : "))

# description
area = 2*length*width + 2*length*height + 2*width*height
circumference = 4*(length+width+height)
volume = length*width*height

# output
print ("######################################")
print ("Its area is ==>",area)
print ("The circumference is ==>",circumference)
print ("The volume is ==>",volume)
print ("#######################################")
again()
