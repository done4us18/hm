#!/bin/sh 

clear

echo -e "\033[1;33m"
echo -e "==========================================="
echo -e "tools termux by Done4us"
echo -e "==========================================="
read -p "Name :" name
echo -e "Welcome sir" $name
echo -e "loading....."
sleep 5
echo -e "\033[1;37m"
echo -e "\033[1;32m"
clear
echo -e "==========================================="
echo -e "menu :"
echo -e ""
echo -e "[1]. install python"
echo -e "[2]. install git"
echo -e "[3]. install php"
echo -e "[4]. quiz"
echo -e "[5]. 1 silent text clock"
echo -e "[0]. exit"
echo -e "==========================================="
read -p "options :" select


if [ $select = 1 ]
then
    echo -e "installing python....."
    echo -e "\033[1;37m"
    cd $HOME
    apt update && apt upgrade
    apt install python
    echo -e "installing done
    echo -e "Thank you for using the tools"
    echo -e "loading..."

    sleep 5
elif [ $select = 2 ]
then
    echo -e "\033[1;37m"
    clear
    echo -e "installing git....."
    cd $HOME
    apt update && apt upgrade
    apt install git
    echo -e "installing done"
    echo -e "Thank you for using the tools"
    echo -e "loading..."
    sleep 5
elif [ $select = 3 ]
then
    echo -e "\033[1;37m"
    clear
    echo -e "installing php....."
    cd $HOME
    apt update && apt upgrade
    apt install php
    echo -e "installing done"
    echo -e "Thank you for using the tools"
    echo -e "loading..."
    sleep 5
elif [ $select = 4 ]
then
    clear
    echo -e "\033[1;32m"
    clear
    echo -e "==========================================="
    echo -e "tools termux by Done4us, access to youtube"
    echo -e "https://www.s.id/ch-subb"
    echo -e "==========================================="
    echo -e "Quiz not yet available"
    echo -e "Quiz will be made on August 17, 2022"
    echo -e "by github.com/done4us"
    echo -e "out in 5 seconds"
    echo -e "\033[1;37m"
    sleep 5
elif [ $select = 5 ]
then
    echo -e "\033[1;31m"
    clear
    echo -e "==========================================="
    echo -e "SUBSCRIBE CHANNEL DONE4US"
    echo -e "==========================================="
    echo -e "the link is shortened to make it easier: https://www.s.id/ch-subb"
    echo -e "out in 1 hour"
    echo -e "new terminal if you want to enter a new script"
    echo -e "\033[1;37m"
    sleep 3600
elif [ $select = 0 ]
then
    clear
    echo -e "\033[1;32Thank you for visiting our tools"
    echo -e "\033[1;37m"
    sleep 3
    clear 
    echo -e "loading"
    sleep 2
    clear
    echo -e "loading."
    sleep 2
    clear 
    echo -e "loading.."
    sleep 2
    clear
    echo -e "loading..."
    sleep 2
    clear
    echo -e "loading...."
    sleep 2
    clear 
    echo -e "loading....."
    sleep 2
    clear
    sleep 1
else
    echo -e ""
    echo -e "\033[1;31mJawaban $select not available sir $name"
    echo -e "\033[1;37m"
    sleep 5
    clear 
    echo -e "- loading."
    sleep 2
    clear
    echo -e "\ loading.."
    sleep 2
    clear 
    echo -e "/ loading..."
    sleep 2
    clear
    echo -e "- loading."
    sleep 2
    clear
    echo -e "\ loading.."
    sleep 2
    clear 
    echo -e "/ loading..."
    sleep 2
    clear
    echo -e "- loading..."
    sleep 3
    clear
fi
