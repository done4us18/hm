import os,sys,time

def clean():
    os.system("clear")

def menu():
    print ("\t==================")
    print ("\t Tools by Done4us")
    print ("\t==================\n")
    print ("1. update")
    print ("2. Upgrade")
    print ("3. Exit")
    #input
    choose = input("Enter the choosen number : ")
    if choose =="1":
        os.system("pkg update")
    if choose =="2":
        os.system("pkg upgrade")
    if choose =="3":
        sys.exit


clean()
menu()
