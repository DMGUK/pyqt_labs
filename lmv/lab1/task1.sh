#!/bin/bash

echo "Number of numbers from 35 to 87 that have a remainder 1, 2 and 5 after division on 7 : "

for i in $(seq 35 87)
do
    remainder=$((i % 7))
    if [ $remainder -eq 1 ] || [ $remainder -eq 2 ] || [ $remainder -eq 5 ]
    then
        echo -n "$i "
    fi
done
echo 