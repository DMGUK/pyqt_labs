#!/bin/bash

function is_point_inside_circle {
    local x=$1
    local y=$2
    local center_x=$3
    local center_y=$4
    local radius=$5

    local distance_squared=$(( (x - center_x) * (x - center_x) + (y - center_y) * (y - center_y) ))

    if (( distance_squared <= radius * radius )); then
        return 0  
    else
        return 1  
    fi
}

echo "Enter the coordinates of the rectangle : "
read x1
read y1
read x2
read y2

echo "Enter the coordinates of the circle and its radius : "
read center_x
read center_y
read radius

if is_point_inside_circle $x1 $y1 $center_x $center_y $radius &&
   is_point_inside_circle $x1 $y2 $center_x $center_y $radius &&
   is_point_inside_circle $x2 $y1 $center_x $center_y $radius &&
   is_point_inside_circle $x2 $y2 $center_x $center_y $radius; then
    echo "The circle belongs to the area of the rectangle."
else
    echo "The circle doesn't belong to the area of the rectangle."
fi
