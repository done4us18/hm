#!/bin/bash

# indian = seconds
second=0
# indian = minute
minute=0
# indian = hours
hour=0

# while loop/
while [[ true ]]
do
 clear
 if (( $second < 60 ))
 then
   (( second++ ))
 elif [ $second -eq 60 ]
 then
   second=0
   (( minute++ ))
 elif [ $minute -eq 60 ]
 then
   minute=0
   (( hour++ ))
 fi
 echo "       [ Stopwatch by Done4us ]"
 echo "hour: $hour minute: $minute second: $second"
 sleep 1
done
