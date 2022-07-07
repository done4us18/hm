#module

import os,sys,time


def slowprints(a):
    for b in a + '\n':
        sys.stdout.write(b)
        sys.stdout.flush()
        time.sleep(0.001)

os.system("clear")
time.sleep(1)

#####################################################################################

#loading effect
def load():
    load = '\033[1;91m.'
    count = 0
    for t in range(20):
             time.sleep(0.3)
             print(f'\r \033[1;91m[\033[0m●\033[1;91m] \033[0mLoading {load}', end='', flush=True)
             count += 1
             if count == 3:
                count = 0
                load += '.'
    print('\n')


######################################################################################

# Banner
def banner():
    slowprints('''

\033[1;91m ████████ ██   ██ ███████ \033[0m ███    ███ ███████ 
\033[1;91m    ██    ██   ██ ██      \033[0m ████  ████ ██      
\033[1;91m    ██    ███████ █████   \033[0m ██ ████ ██ █████ 
\033[1;91m    ██    ██   ██ ██      \033[0m ██  ██  ██ ██    
\033[1;91m    ██    ██   ██ ███████ \033[0m ██      ██ ███████

\033[1;91m ●\033[0m Author  Rs1819             \033[1;90m Version 0.7.2
\033[1;91m ●\033[0m YouTube Done4us''')

#####################################################################################

# Installed Successfully
def inst():
    os.system("clear")
    banner()
    print("")
    print("\033[0m Theme Installed \033[1;92mSuccessfully \033[0m!")
    print("")
    input("\033[0m [\033[1;91mhome\033[0m~\033[0;90mtheme\033[0m] > ")
    time.sleep(1)
    print("")

######################################################################################

#skull name
def skull_name():
    os.system("clear")
    banner()
    print("")
    user = input(" [\033[1;91m•\033[0m] Username    : ")
    time.sleep(0.3)
    prompt = input(" [\033[1;91m•\033[0m] Prompt Name : ")
    print("")
    time.sleep(1)
    load()
    inst()
    skull_copy(user)

#######################################################################################

# skull1

def skull():
    skull_name()

def skull_copy(user):
        with open("done4us.py","w") as external_file:
            add_text ='''\n

######################################

g = "\\033[32;1m"
gt = "\\033[0;32m"
bt = "\\033[34;1m"
b = "\\033[36;1m"
m = "\\033[31;1m"
c = "\\033[0m"
p = "\\033[37;1m"
u = "\\033[35;1m"
M = "\\033[3;1m"
k = "\\033[33;1m"
kt = "\\033[0;33m"
a = "\\033[30;1m"

W = "\\x1b[0m"
R = "\\x1b[31m"
G = "\\x1b[1;32m"
O = "\\x1b[33m"
B = "\\x1b[34m"
P = "\\x1b[35m"
C = "\\x1b[36m"
GR = "\\x1b[37m"

#######################################

#module
import os,sys,time

def slowprints(a):
    for b in a + '\\n':
        sys.stdout.write(b)
        sys.stdout.flush()
        time.sleep(0.001)

os.system("clear")
time.sleep(1)


def skull(user):
    slowprints(f"""
                    {m} uuuuu
                uu$$$$$$$$$$$uu
             uu$$$$$$$$$$$$$$$$$uu
            u$$$$$$$$$$$$$$$$$$$$$u
           u$$$$$$$$$$$$$$$$$$$$$$$u
          u$$$$$$$$$$$$$$$$$$$$$$$$$u
          u$$$$$$$$$$$$$$$$$$$$$$$$$u
          u$$$$$$“   “$$$“   “$$$$$$u
          “$$$$“      u$u       $$$$“
           $$$u       u$u       u$$$
           $$$u      u$$$u      u$$$
            “$$$$uu$$$   $$$uu$$$$“
             “$$$$$$$“   “$$$$$$$“
               u$$$$$$$u$$$$$$$u
                u$“$“$“$“$“$“$u
     uuu        $$u$ $ $ $ $u$$       uuu
    u$$$$        $$$$$u$u$u$$$       u$$$$
     $$$$$uu      “$$$$$$$$$“     uu$$$$$$
   u$$$$$$$$$$$uu    “““““    uuuu$$$$$$$$$$
   $$$$“““$$$$$$$$$$uuu   uu$$$$$$$$$“““$$$“
    “““      ““$$$$$$$$$$$uu ““$“““
              uuuu ““$$$$$$$$$$uuu
     u$$$uuu$$$$$$$$$uu ““$$$$$$$$$$$uuu$$$
     $$$$$$$$$$““““           ““$$$$$$$$$$$“
      “$$$$$“                      ““$$$$““
   {a}...::::[ Powered by Done4us YouTube ]::::...{W}
            {W} [\\033[1;41m  Username : {user}  {W}]""")

skull(user)'''
            print(f'user = "{user}"\n', add_text, file=external_file)
            external_file.close()

######################################################################################

# Choose
def choose():
    print("")
    no = input("\033[0m [\033[1;91mhome\033[0m~\033[0;90mtheme\033[0m] > ")
    if no == '1' or no == '01':
       skull()
    else:
       menu()

######################################################################################

# Tool Menu
def menu():
    os.system("clear")
    banner()
    slowprints('''\033[91m╔═════════════\033[0m•─[\033[1;41m LIST THEME \033[0m]─•\033[91m════════════•
│
├─[\033[0m1\033[1;91] \033[0mSkull
\033[1;91m├─────────────────────────[\033[0m2\033[1;91m] \033[0mSkull(1)
\033[1;91m├─[\033[0m3\033[1;91m] \033[0mAnonymous
\033[1;91m├─────────────────────────[\033[0m4\033[1;91m] \033[0mGithub
\033[1;91m├─[\033[0m5\033[1;91m] \033[0mDragon
\033[1;91m├─────────────────────────[\033[0m6\033[1;91m] \033[0mDog
\033[1;91m├─[\033[0m7\033[1;91m] \033[0mUmbrella
\033[1;91m├─────────────────────────[\033[0m8\033[1;91m] \033[0mGeometric
\033[1;91m│
├─[\033[0m9\033[1;91m] \033[0mSupport Me On \033[1;41m YouTube \033[0m
\033[1;91m└─[\033[0m0\033[1;91m] \033[0mExit''')
    choose()

#######################################################################################

# login function
def login():
    banner()
    password = input("""\033[0m╔══════════⟨ \033[1;41m L O G I N  T O O L S \033[0m ⟩══════════•
│
└─⟩ """)
    if password == 'done4us':
       time.sleep(2)
       print("")
       print("\033[1;92m✓ \033[0mLogin Success")
       time.sleep(1)
       print("")
       os.system("clear")
       time.sleep(0.8)
       menu()
    else:
       time.sleep(2)
       print("")
       print("\033[1;91mX \033[0mLogin Failed")
       time.sleep(2)
       os.system("python test1.py")

########################################################################################

login()
