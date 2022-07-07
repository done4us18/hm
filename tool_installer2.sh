 #!/bin/bash

clear

echo "[1] Install Python"
echo "[2] Install Bash"
echo "[3] Exit"
echo ""
read -p "choose : " choose
if [ $choose = "1" ]
then
     echo "Installing..."
     sleep 2
     cd $HOME
     apt install python -y

elif [ $choose = "2" ]
then
      echo "Installing..."
      sleep 2
      cd $HOME
      apt install bash -y

elif [ $choose = "3" ]
then
      echo "thank you for using this tool"
      sleep 1
      echo "don't forget to subscribe everyone"
      sleep 1
      echo "by Done4us"
      sleep 1
      exit
else
     echo "select the correct input "
     sleep 2
     bash tool_installer2.sh
fi
