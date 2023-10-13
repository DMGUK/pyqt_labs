#!/bin/bash

sum_positive_elements() {
    local arr=("$@")  

    local sum=0

    local num=0

    for element in "${arr[@]}"; do
        if [[ $element -gt 0 ]]; then
            sum=$((sum + element))
            num=$((num + 1))
        fi
    done

    echo "Number of positive elements: $num"
    echo "Sum of positive elements: $sum"
}

read -p "Enter the number of rows: " rows
read -p "Enter the number of columns: " columns

input_array=()

for ((i=0; i<rows; i++)); do
    for ((j=0; j<columns; j++)); do
        read -p "Enter element at index [$i,$j]: " element
        input_array+=($element)
    done
done

sum_positive_elements "${input_array[@]}"
