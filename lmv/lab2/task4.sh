#!/bin/bash

SumDigit() {
    local num=$1
    local sum=0

    while [ $num -gt 0 ]; do
        sum=$((sum + num % 10))
        num=$((num / 10))
    done

    echo $sum
}

SumRange() {
    local a=$1
    local b=$2
    local total_sum=0

    for ((i=a; i<=b; i++)); do
        local current_sum=$(SumDigit $i)
        total_sum=$((total_sum + current_sum))
    done

    echo $total_sum
}

read -p "Enter the first number: " num1
read -p "Enter the second number: " num2
result=$(SumRange $num1 $num2)

echo "Sum of digits in the range of [$num1, $num2]: $result"

