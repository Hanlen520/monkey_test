@echo off
setlocal enabledelayedexpansion
for /F "eol=* tokens=*" %%i in ('netstat -an -o ^| findstr "5037"') do (
set a=%%i
set a=!a:~69,10!
taskkill /t /f /pid !a!
)
pause>nul