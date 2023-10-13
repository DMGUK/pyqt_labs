#!/bin/bash

gcd() {
    a=$1
    b=$2

    while [ $b -ne 0 ]; do
        temp=$b
        b=$((a % b))
        a=$temp
    done

    echo $a
}

read -p "Enter the first number: " num1
read -p "Enter the second number: " num2

result=$(gcd $num1 $num2)

echo "GCD of numbers $num1 and $num2 is: $result"

