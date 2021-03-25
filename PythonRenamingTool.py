import subprocess

    subprocess.Popen("adb shell input tap 921 2265", shell = True)                   ##three lines
    subprocess.Popen("adb shell input tap 955 1871", shell = True)                   ##appraise
    subprocess.Popen("adb shell input tap 749 1782", shell = True)
    subprocess.Popen("adb shell sleep 2", shell = True)
    subprocess.Popen("adb shell input tap 420 1444", shell = True)
    subprocess.Popen("adb shell input tap 530 1030", shell = True)                   ##Open nameline 
    subprocess.Popen("adb shell swipe 986 2090 990 2090 1000", shell = True)         ##Delete all text from nameline
    subprocess.Popen("adb shell input swipe 782 1475 782 1475 583", shell = True)    ##Hold nameline
    subprocess.Popen("adb shell input tap 132 1374", shell = True)                   ##Paste new name
    subprocess.Popen("adb shell input tap 955 1490", shell = True)                   ##Ok Keyboard       
    subprocess.Popen("adb shell input tap 550 1360", shell = True)                   ##Ok PokemonGo App
    subprocess.Popen("adb shell input tap 550 1360", shell = True)                   ##Ok PokemonGo App
    subprocess.Popen("adb shell input swipe 1022 1376 645 1354 564", shell = True)   ##Next Pokemon

