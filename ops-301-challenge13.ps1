#Geneva Knott 
# I worked with Sierra M, Justin H, and Nick A
# Auto New Users
# https://blog.netwrix.com/2018/06/07/how-to-create-new-active-directory-users-with-powershell/
# 29Mar23

Import-Module ActiveDirectory
New-ADUser -Name "Franz Ferdinand" -GivenName "Franz" -Surname "Fredinand" -SamAccountName "Franz.F" -UserPrincipalName "fredi@GlobeXpower.com" -AccountPassword (Read-Host -AsSecureString "Input Password") -Enabled $true
Get-ADUser Franz.F