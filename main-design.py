#module
import os,sys,time

def slowprints(a):
    for b in a + '\n':
        sys.stdout.write(b)
        sys.stdout.flush()
        time.sleep(0.001)

os.system("clear")
time.sleep(1)


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


# names
def name():
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

# skull1
def skull1():
    name()
    slowprints("""
                     uuuuu
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
   ...::::[ Powered by Done4us YouTube ]::::...
          [\033[1;41  Username : {user}  \033[0m]
""")


# Choose
def choose():
    print("")
    no = input("\033[0m [\033[1;91mhome\033[0m~\033[0;90mtheme\033[0m] > ")
    if no == '1' or no == '01':
       skull1()


# Tool Menu
def menu():
    os.system("clear")
    banner()
    slowprints('''\033[91m╔═════════════\033[0m•─[\033[1;41m LIST THEME \033[0m]─•\033[91m════════════•
│
├─[\033[0m1\033[1;91] \033[0mSkull(1)
\033[1;91m├─────────────────────────[\033[0m2\033[1;91m] \033[0mSkull(2)
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
       os.system("python design.py")
login()
