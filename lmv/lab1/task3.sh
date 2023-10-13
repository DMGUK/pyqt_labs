#!/bin/bash

read -p "Enter the first side of the triangle: " a
read -p "Enter the second side of the triangle: " b
read -p "Enter the third side of the triangle: " c

if [ "$a" -eq "$b" ] && [ "$b" -eq "$c" ]; then
    echo "It's an equal-side triangle."
    exit
fi

if [ "$a" -eq "$b" ] || [ "$b" -eq "$c" ] || [ "$a" -eq "$c" ]; then
    echo "It's an equal-leg triangle."
    exit
fi

if [ "$a" -gt "$b" ] && [ "$a" -gt "$c" ]; then
    hypotenuse="$a"
    side1="$b"
    side2="$c"
elif [ "$b" -gt "$a" ] && [ "$b" -gt "$c" ]; then
    hypotenuse="$b"
    side1="$a"
    side2="$c"
else
    hypotenuse="$c"
    side1="$a"
    side2="$b"
fi

if [ $((side1*side1 + side2*side2)) -eq $((hypotenuse*hypotenuse)) ]; then
    echo "It's an right triangle."
else
    if [ $((side1*side1 + side2*side2)) -lt $((hypotenuse*hypotenuse)) ]; then
        echo "It's an obtuse triangle."
    else
        echo "It's an acute triangle."
    fi
fi
