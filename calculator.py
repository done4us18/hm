import os,sys,time,subprocess

#list menu
def Addition(y,x):
    return y+x
def Multiplication(y,x):
    return y*x
def Division(y,x):
    return y/x
def Subtraction(y,x):
    return y-x

    number_1 = int(input("Enter the first number ~> "))
    number_2 = int(input("Enter the second number ~> "))

# menu
print("+--------------------------------------+")
print("[1] Addition")
print("[2] Multiplicaton")
print("[3] Division")
print("[4] Subtraction")
print("[0] Exit")
choose = input("choose from menu ~> ")

# menu
# this is for addition
if choose =="1":
    number_1 = int(input("Enter the first number ~> "))
    number_2 = int(input("Enter the second number ~> "))
    print(number_1,"+",number_2,"=",Addition(number_1,number_2))
elif choose =="2":
    number_1 = int(input("Enter the first number ~> "))
    number_2 = int(input("Enter the second number ~> "))
    print(number_1,"*",number_2,"=",Multiplication(number_1,number_2))
elif choose =="3":
    number_1 = int(input("Enter the first number ~> "))
    number_2 = int(input("Enter the second number ~> "))
    print(number_1,"/",number_2,"=",Division(number_1,number_2))
elif choose =="4":
    number_1 = int(input("Enter the first number ~> "))
    number_2 = int(input("Enter the second number ~> "))
    print(number_1,"-",number_2,"=",Subtraction(number_1,number_2))
elif choose =="0":
   print("Thank you for using this tool")
   os.system("sleep 0.6")
   print("Don't forget to subcribe everyone")
   os.system("sleep 1")
   sys.exit()
else:
   print("Choose the correct input")
   os.system("clear")
   os.system("python calculator.py")

