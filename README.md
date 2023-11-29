# README

> Push you git repository in real quick!



## Description

A bash script that helps you ease your "git push". There will be a powershell version for windows environment soon. 


## Usage

1. Copy `quick_git_push.sh` into a safe directory.
2. Add `alias push='. <directory_to_quick_git_push.sh>/quick_git_push.sh'` into your `.bashrc` or `.bash_aliases` profile. You can modify *"push"* to any other alias you like.
3.  `$ cd <your_git_repo>`, run the alias in terminal: `$ push` (*"push"* in my case, make sure the .`bashrc` profile is sourced before using)：



## Notice!

As shown blow, the git commit format is fixed, so **do not use this script in projects with strict commit format requirements.**



Inside `quick_git_push.sh`, as a reference to the commit message:

```bash
......

# Get date from your computer system
today=$(date +"%y.%m.%d")

# execute git commit
git commit -m "update $today"

......
```

