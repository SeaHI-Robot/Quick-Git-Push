# Get today's date in the format "YYYY-MM-DD"
$today = Get-Date -Format "yyyy-MM-dd"

Write-Host " "
Write-Host "Today is: $today"
Write-Host "---------------------------------------------"
Write-Host "This powershell script eases your git push process."
Write-Host "---------------------------------------------"
Write-Host " "





# Execute git add .
git add .

# Execute git commit
git commit -m "update $today"

# Execute git push
git push
