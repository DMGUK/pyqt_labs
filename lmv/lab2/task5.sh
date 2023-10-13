#!/bin/bash

calculate_b_values() {
    local b1=0
    local b2=0
    local b3=0
    local b4=0
    local b5=0
    local b6=0
    local b7=0
    local b8=0
    local b9=0
    local b10=0

    for i in {1..24}; do
        a="$1"  
        b1=$(echo "scale=10; $b1 + $a" | bc)
        b2=$(echo "scale=10; $b2 + ($a * $a)" | bc)
        b3=$(echo "scale=10; $b3 + ($a ^ 3)" | bc)
        b4=$(echo "scale=10; $b4 + ($a ^ 4)" | bc)
        b5=$(echo "scale=10; $b5 + ($a ^ 5)" | bc)
        b6=$(echo "scale=10; $b6 + ($a ^ 6)" | bc)
        b7=$(echo "scale=10; $b7 + ($a ^ 7)" | bc)
        b8=$(echo "scale=10; $b8 + ($a ^ 8)" | bc)
        b9=$(echo "scale=10; $b9 + ($a ^ 9)" | bc)
        b10=$(echo "scale=10; $b10 + ($a ^ 10)" | bc)

        shift  
    done

    echo "The given sequence is : "

    echo "b1 = $b1"
    echo "b2 = $b2"
    echo "b3 = $b3"
    echo "b4 = $b4"
    echo "b5 = $b5"
    echo "b6 = $b6"
    echo "b7 = $b7"
    echo "b8 = $b8"
    echo "b9 = $b9"
    echo "b10 = $b10"
}

input_array=()

for ((i=1; i<=24; i++)); do
    read -p "Enter element at index [$i]: " element
    input_array+=($element)
done

calculate_b_values "${input_array[@]}"
