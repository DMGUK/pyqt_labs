#!/bin/bash

selected=$(zenity --list --checklist \
                --title="Choose programs for installing" \
                --column="Choice" --column="Program" --column="Description" \
                TRUE "vim" "Text editor" \
                TRUE "htop" "System monitoring" \
                TRUE "curl" "URL downloader" \
                TRUE "figlet" "Create ASCII text banners" \
                TRUE "googler" "Google from the linux terminal" \
                TRUE "nms" "Show data decryption screen" \
                --width=300 \
                --height=200)

if [ -z "$selected" ]; then
    zenity --info \
    --title="Info" \
    --text="You didn't choose any program" \
    --width=300 \
    --height=200
    exit 0
fi

for program in $selected; do
    if dpkg -l | grep -q "^ii  $program "; then
        zenity --info \
        --title="Info" \
        --text="The program $program is already installed" \
        --width=300 \
        --height=200
    else
        sudo apt install -y $program
        zenity --info --title="Info" --text="Program was installed successfully" --width=300 --height=200
    fi
done

exit 0
