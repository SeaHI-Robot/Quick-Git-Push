# README

> Push you git repository in real quick!



## Description

A bash script that helps you ease your "git push". 



## Usage

1. Copy `quick_git_push.sh` into a safe directory.
2. Add `alias push='. <directory_to_quick_git_push.sh>/quick_git_push.sh'` into your `.bashrc` or `.bash_aliases` profile. You can modify *"push"* to any other alias you like.



## Notice!

As shown blow, the git commit format is fixed, so **do not use this script in projects with strict commit format requirements.**



Inside `quick_git_push.sh`:

```bash
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
```

