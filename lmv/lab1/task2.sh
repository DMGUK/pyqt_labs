#!/bin/bash

i=1
sum=0

echo "Enter numbers"
while [ $i -le 20 ]
do
    read num
    if [ $((num % 2)) -ne 0 ]   
    then
        sum=$((sum + 1))
    fi
    i=$((i + 1)) 
done

echo "Number of odd numbers entered in a sequence: $sum"
