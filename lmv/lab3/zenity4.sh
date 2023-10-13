#!/bin/bash

selected_directory=$(zenity \
    --file-selection \
    --directory \
    --title="Choose a folder")

if [ $? -eq 1 ]; then
    zenity --info \
        --title="Info" \
        --text="You didn't choose any folder"
    exit 0
fi

if [ ! -d "$selected_directory" ]; then
    zenity --info \
        --title="Info" \
        --text="This element is not a folder"
    exit 0
fi

search_string=$(zenity \
    --entry \
    --title="Select a row for search" \
    --text="Select a row for search in files:" \
    --width=300 \
    --height=200)

if [ -z "$search_string" ]; then
    zenity --info \
        --title="Info" \
        --text="You didn't enter any text" \
        --width=300 \
        --height=200
    exit 0
fi

result=$(grep -rl "$search_string" "$selected_directory")
info=""

for file in $result; do
    size=$(du -h "$file" | cut -f1)
    info="$info$file ($size)\n"
done

if [ -z "$info" ]; then
    zenity --info \
        --title="Info" \
        --text="There aren't any files that contain the given text" \
        --width=300 \
        --height=200
else
    zenity --info \
        --title="Info" \
        --text="Full path and name of each file that contain the given text:\n$info" \
        --width=300 \
        --height=200
fi

exit 0
