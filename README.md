# README

> Push you git repository in real quick!



## Description

Bash/PowerShell scripts that help you ease your "git push" process. 

The scripts were tested and work well on ubuntu & windows environments.



## Usage

<details>   
    <summary>Bash - ubuntu</summary>
    1. Copy `quick_git_push.sh` into a safe directory.
    2. Add `alias push='. <directory_to_quick_git_push.sh>/quick_git_push.sh'` into your `.bashrc` or `.bash_aliases` profile. You can modify *"push"* to any other alias you like.
    3. `$ cd <your_git_repo>`, run the alias in Bash terminal: `$ push` (*"push"* in my case, make sure the .`bashrc` profile is sourced before using)： </details>




<details>
    <summary>powershell - windows</summary>
    1.  Run `Set-ExecutionPolicy RemoteSigned
` in your PowerShell to make sure PowerShell scripts with the suffix `.ps1` are executable. (Administrator privileges may be required)
    2.  In PowerShell, run`$PROFILE` to find the directory to the Powershell profile `Microsoft.PowerShell_profile.ps1Microsoft.PowerShell_profile.ps1`, if it doesn't exit, run `New-Item -Type File -Path $profile -Force` to create it.
    3.  Copy `quick_git_push.ps1` into a safe directory.
    4.  Add `New-Alias -Name push -Value <directory_to_quick_git_push.sh>\quick_git_push.ps1` into `Microsoft.PowerShell_profile.ps1`. You can modify *"push"* to any other alias you like.
    5. `cd <your_git_repo>`, run the alias in PowerShel terminall: `$ push` (*"push"* in my case)
</details>



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

