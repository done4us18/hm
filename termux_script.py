import os
import random
import sys
import time
from time import sleep

os.system('clear')
def type(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
print ('Loading..')
sleep(0.1)
type('> > > > > > > > > > > > > > >] 100%')
sleep(1)
os.system('clear')
def main():
    password = input ('Enter keywords : ')
    if password == 'done4us':
        print ('Password accepted')
        sleep(2)
        os.system('clear')
    else:
        print ('password not matched')
        os.system("python termux_script.py")
main()
sleep(1)
os.system('clear')

#banner
print('\033[34m')
print('           ooooooooooo')
sleep(0.1)
print('         oooooooooooooooo')
sleep(0.1)
print('       ooooooooooooooooooooo')
sleep(0.1)
print ("	\033[00m||~~~~~~~~~~~~~>>\033[1;31mWRITTEN by DONE4US\033[00m<<~~~~~~~~~~~~~||\n")

print ('Study 1')
print ('Study 2')
print ('Study 3')
def main():
    choice = input ('Enter your choice :')
    if choice == '1' or choice == '01':
     os.system('clear')
     print ('loading..')
     type ('> > > > > > > > > > > >] 100%')
     print ('Installing data')
     os.system('pkg update -y && pkg upgrade -y')
main()
