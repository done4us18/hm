#!/bin/bash
figlet  _Done4us_ | lolcat
figlet _channel_ | lolcat
date | lolcat
echo "-----------------------------------------------------------" | lolcat
sleep 2
echo
read -p "Enter the password :" pass;
while [ $pass = 'done4us' ]
do
	echo "	 ===== MENU ====="
	echo "	[1] Install python"
	echo "	[2] Install ruby"
	echo "	[3] Exit"
	echo "	================"
echo -n "Enter your choice :"
read enter;
if [ $enter = '1' ] || [ $enter = '01' ]:
then
	pkg install python -y
elif [ $enter = '2' ] || [ $enter = '02' ]:
then
	pkg install ruby -y
elif [ $enter = '3' ] || [ $enter = '03' ]:
then
	echo "Thank You"
	exit
fi

done
