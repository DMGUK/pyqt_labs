#!/bin/bash

directory=$(
    zenity --file-selection \
    --directory \
    --title="Choose a folder"
)

if [ $? -eq 1 ]; then
    zenity --info \
    --title="Info" \
    --text="You didn't choose any folder" \
    --width=300 \
    --height=200
    exit 0
fi

oversized_files=$(find "$directory" -type f -size +5M)

if [ -n "$oversized_files" ]
then
    zenity --info \
    --title="Info" \
    --text="Files in a given folder that are larger than 5 Mb:\nFolder : $directory \n$oversized_files" \
    --width=300 \
    --height=200
else
    zenity --info \
    --title="Info" \
    --text="There aren't any files in this folder that are larger than 5 Mb \nFolder : $directory" \
    --width=300 \
    --height=200
fi
exit 0

