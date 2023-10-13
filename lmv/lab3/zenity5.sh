#!/bin/bash

questions=(
    "Which function is the most important one in C++?\nA. function\nB. main\nC. defmain\nD. func\nE. mostimp"
    "How to import a library in C++?\nA. #from\nB. #import\nC. #require\nD. #lib\nE. #include"
    "What does OOP mean?\nA. Object-Oriented Programming\nB. Object-Oriented Protocol\nC. Object-Oriented Process\nD. Object-Oriented Page\nE. Object-Oriented Politics"
    "What is a keyword for integer varialbles in C++?\nA. class\nB. float\nC. int\nD. class\nE. file"
    "What C++ library is used for I/O operations?\nA. math.h\nB. fstream\nC. stdio.h\nD. iostream\nE. time.h"
)

answers=(
    "B"
    "E"
    "A"
    "C"
    "D"
)

score=0

for i in "${!questions[@]}"; do
    question="${questions[$i]}"
    correct_answer="${answers[$i]}"

    user_answer=$(zenity --list --radiolist \
                    --title="C++ Test" \
                    --text="$question" \
                    --column="Choice" --column="Answer" \
                    FALSE "A" FALSE "B" FALSE "C" FALSE "D" FALSE "E"\
                    --width=600 --height=400)

    if [ "$user_answer" = "$correct_answer" ]; then
        score=$((score+1))
    fi
done

if [ $score -ge 0 ] && [ $score -le 2 ]; then
    zenity --info \
    --title="Test result" \
    --text="You scored $score from ${#questions[@]} points. \
    \nYour result is very bad. \
    \nPlease, do some practice and try again later" \
    --width=300 \
    --height=200
elif [ $score == 3 ]; then
    zenity --info \
    --title="Test result" \
    --text="You scored $score from ${#questions[@]} points. \
    \nYour result is not very bad but you should practice. \
    \nPlease, try again later" \
    --width=300 \
    --height=200
elif [ $score == 4 ]; then
    zenity --info \
    --title="Test result" \
    --text="You scored $score from ${#questions[@]} points. \
    \nYour result is good but you still need some practice. \nPlease, try again later !!!" \
    --width=300 \
    --height=200
else
    zenity --info \
    --title="Test result" \
    --text="You scored $score from ${#questions[@]} points. \
    \nYour result is very good. \nCongratulations !!!" \
    --width=300 \
    --height=200
fi
exit 0

