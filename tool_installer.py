import os,sys,time

def again():
      f = input("Do you want to Continue [y/n] : ")
      if f == "y":
          os.system("python tool_installer.py")
      elif f == "n":
          sys.exit()

def clean():
      os.system("clear")

def menu():
      clean()
      print ("\033[1;94m+\033[1;93m-----------------------------------------------\033[1;94m +")
      print ("\033[1;96mAuthor    \033[1;91m: \033[1;93mDone4us & Om kant mani")
      print ("\033[1;96mYoutube   \033[1;91m: \033[1;93mDone4us & Om kant mani")
      print ("\033[1;96mFacebook  \033[1;91m: \033[1;93mhttps://www.facebook.com/done4us18")
      print ("\033[1;96mInstagram \033[1;91m: \033[1;93mhttps://www.instagram.com/done4us18")
      print ("\033[1;96mGithub    \033[1;91m: \033[1;93mhttps://github.com/done4us")
      print ("\033[1;94m+\033[1;93m------------------------------------------------\033[1;94m+")
      print ("\033[1;90m[\033[1;95m1\033[1;90m] \033[1;93mInstall Neofetch")
      print ("\033[1;90m[\033[1;95m2\033[1;90m] \033[1;93mInstall Screenfetch")
      print ("\033[1;90m[\033[1;95m3\033[1;90m] \033[1;93mExit")
      choose = input("\033[1;96mchoose by Number \033[1;90m~\033[1;95m>\033[1;92m ")

      if choose == "1":
         os.system("pkg update -y && pkg upgrade -y")
         os.system("pkg install git -y")
         os.system("pkg install python -y")
         os.system("pkg install neofetch")
         again()
      elif choose == "2":
          os.system("pkg update -y && pkg upgrade -y")
          os.system("pkg install git -y")
          os.system("pkg install bash")
          os.system("pkg install screenfetch")
          again()
      elif choose == "3":
          sys.exit()
      else:
         print("select the correct input")
         os.system("python tool_installer.py")
menu()
