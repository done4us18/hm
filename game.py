# module
import os,sys,time,random

def again():
    f = input("Apakah anda Ingin Mengulang [y/n] : ")
    if f =="y":
        os.system("python game.py")
    elif f =="n":
        print("Thank you for playing this game")
        sys.exit()

# menu
def menu():
    os.system("clear")
    print ("\033[1;93m\t Choose Menu\n")
    print ("\033[1;90m[\033[1;96m1\033[1;90m] \033[1;95mstone")
    print ("\033[1;90m[\033[1;96m2\033[1;90m] \033[1;95mscissor")
    print ("\033[1;90m[\033[1;96m3\033[1;90m] \033[1;95mpaper")
    comp = random.choice(("stone","scissor","paper"))
    choose = input("\033[1;96mSelect the input \033[1;91m: \033[1;95m")
    # stone
    if choose =="1":
        print ("You      : stone")
        print ("computer : ",comp)
        if comp =="stone":
            print ("Draw")
        elif comp =="scissor":
            print ("You Win")
        elif comp =="paper":
            print ("YOu lose")
        again()
    # scissor
    if choose =="2":
        print ("You      : scissor")
        print ("Computer : ",comp)
        if comp =="stone":
            print ("You lose")
        elif comp =="scissor":
            print ("Draw")
        elif comp ==("paper"):
            print ("You Win")
        again()
    # paper
    if choose =="3":
        print ("You      : paper")
        print ("Computer : ",comp)
        if comp =="stone":
            print ("You win")
        elif comp =="scissor":
            print ("You lose")
        elif comp =="paper":
            print ("Draw")
        again()

    else:
        os.system("clear")
        os.system("python game.py")

menu()
