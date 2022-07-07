#!/bin/bash
echo
echo  "|..........Let's check in this tool's user.........|"
echo
# input password

pas="Hello !! Welcome"
read -p "Enter your Username :" name;
read -p "Enter your password :" pass;
sleep 0.1
echo
#echo $pas $name
sleep 0.1
# CHecking pass word
 if  [ $pass = "done4us" ]
        then
        echo
        echo "PASSWORD MATCHED"
          sleep 0.1
        else
          echo "PSSWORD NOT MATCHED"
        bash login.sh
          sleep 0.1
fi

echo
echo
