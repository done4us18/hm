import os,sys,time

x = "done4us"
y = "done4us"

def login():
    user = input("Enter Username : ")
    pasw = input("Enter Password : ")

    if user ==x and pasw ==y:
        print ("Access Granted")
        time.sleep(2)
    else:
        print ("Access Denied")
        time.sleep(2)
        os.system("clear")
        os.system("python password_check.py")

if __name__ == "__main__":
    login()
