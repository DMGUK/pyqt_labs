#!/bin/bash

file=$(
    zenity --file-selection \
        --title="Choose a file : "
)

if [ $? -eq 1 ]; then
    zenity --info \
    --title="Info" \
    --text="You didn't choose any file" \
    --width=300 \
    --height=200
    exit 0
fi

line_count=$(wc -l < "$file")

zenity --info \
    --title="Info" \
    --text="Number of rows in file \"$file\" is : $line_count"

exit 0

