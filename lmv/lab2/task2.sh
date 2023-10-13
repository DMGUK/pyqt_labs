#!/bin/bash

dist() {
    x1=$1
    x2=$2
    y1=$3
    y2=$4

    distance=$(bc <<< "scale=2; sqrt(($x2 - $x1)^2 + ($y2 - $y1)^2)")
    echo $distance
}

read -p "Enter the x coordinate of first point: " coordx1
read -p "Enter the y coordinate of first point: " coordy1

read -p "Enter the x coordinate of second point: " coordx2
read -p "Enter the y coordinate of second point: " coordy2

result=$(dist $coordx1 $coordx2 $coordy1 $coordy2)
echo "Distance between points is: $result"

