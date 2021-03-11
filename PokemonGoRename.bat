set loop=0
:loop
.\adb.exe shell input tap 921 2265 --three lines
.\adb.exe shell input tap 955 1871 --appraise
.\adb.exe shell input tap 749 1782
.\adb.exe shell sleep 2;
.\adb.exe shell input tap 420 1444
.\adb.exe shell input tap 530 1030 --open nameline 
.\adb.exe shell input swipe 986 2090 990 2090 1000 --delete all text from name line
.\adb.exe shell input swipe 782 1475 782 1475 583 --hold nameline
.\adb.exe shell input tap 132 1374 --paste
.\adb.exe shell input tap 955 1490 -- OK keyboard
.\adb.exe shell input tap 550 1360 -- OK pokemon go app
.\adb.exe shell input tap 550 1360 --OK pokemon go app
.\adb.exe shell input swipe 1022 1376 645 1354 564 --next pokemon
set /a loop=%loop%+1 
if "%loop%"=="500" goto next
goto loop