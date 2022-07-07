# module
import os,sys,time,getpass


# username
x = "done4us"
# password
y = "done4us"

# fast auto typing
def sp(a):
    for e in a + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.speed(0.002)

# login
def login():
    
    username = input("{+} Username : ")
    pasword = getpass.getpass("{+} Password : ")
    if username == x and pasword == y:
        print("Access Grandted")
        time.sleep(1)
    else:
        print("Access Denied")
        time.sleep(1)
        login()

login()


