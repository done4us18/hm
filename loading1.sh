#!/bin/sh

R='\x1b[1;31m'

G='\x1b[1;32m'

B='\x1b[1;34m'

Y='\x1b[1;33m'

C='\x1b[1;36m'

D='\x1b[0m'

# Above is a set of color codes used in this script

read -p "Enter your percent value :"
$1 
sleep 4
function Percent(){

    message="$1" #($1) for parameter 1 and and so on

    max=$2 #($2) for parameter 2 and and so on

    #make loop

    while true; do

        i=1

        #-le (less than) or less than

        #0 less than maximum (100)

        #then the statement will be executed from number 1-100

        while [ $i -le $max ]; do

            echo -ne "\r${G}[✓]${C} $message ${G}$i${D} %"

            #if i value is equal to 100 or the maximum limit then it means Perce method / function             >

            #Percent "Loading..." 100

            #will keep repeating

            if [ $i -eq 100 ]; then

                echo -ne "${G} [succeed!]${D}\n"

                Percent "Loading..." 100

            fi

            #increase the value of variable i by 1

            #this is what will be written numbers 1 to 100

            let i++

        done

    done

}

Percent "Loading..." 100
