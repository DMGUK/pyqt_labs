#!/bin/bash

declare -a days_of_week=(
  [0]=1
  [1]=2
  [2]=3
  [3]=4
  [4]=5
  [5]=6
  [6]=7
)

read -p "Enter the number of the day (1-7): " n

day_index=${days_of_week[$((n-1))]}

case $day_index in
    1) echo "Monday is a working day";;
    2) echo "Tuesday is a working day";;
    3) echo "Wednesday is a working day";;
    4) echo "Thursday is a working day";;
    5) echo "Friday is a working day";;
    6) echo "Saturday is a weekend day";;
    7) echo "Sunday is a weekend day";;
    *) echo "Incorrect day. Enter the number from 1 to 7.";;
esac


