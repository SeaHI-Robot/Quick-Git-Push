#!/bin/bash

# Get date from your computer system
today=$(date +"%y.%m.%d")

echo " "

echo "Today is $today"

echo "---------------------------------------------"

echo "This bash script eases your git push process." 

echo "---------------------------------------------"

echo " "


# execute git add
git add .

# execute git commit
git commit -m "update $today"

# execute git push
git push