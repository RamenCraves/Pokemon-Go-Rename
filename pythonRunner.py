import subprocess
from time import sleep

sleepyTime = 0.35


def executeAdbCommand(values):
    cmd = ['./adb.exe', *values]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    process.wait()


def tap(x, y):
    executeAdbCommand(['shell', 'input', 'tap', str(x), str(y)])
    sleep(sleepyTime)


def swipe(xStart, yStart, xEnd, yEnd, time):
    executeAdbCommand(['shell', 'input', 'swipe', str(
        xStart), str(yStart), str(xEnd), str(yEnd), str(time)])
    sleep(sleepyTime)


def hold(x, y, time):
    executeAdbCommand(['shell', 'input', 'swipe', str(
        x), str(y), str(x), str(y), str(time)])
    sleep(sleepyTime)


def pressThreeLines():
    tap(921, 2050)
    sleep(sleepyTime)


def pressAppraise():
    tap(955, 1620)
    sleep(sleepyTime)


def tapSomewhereLeft():
    # TODO: Make this a bit more random
    tap(450, 1700)
    sleep(sleepyTime)


def tapName():
    tap(530, 930)
    sleep(sleepyTime)


def holdBackspace():
    hold(1013, 1866, 998)
    sleep(sleepyTime)


def holdNameLine():
    hold(737, 1134, 583)
    sleep(sleepyTime)


def tapPaste():
    tap(125, 987)
    sleep(sleepyTime)


def tapKeyboardOk():
    tap(960, 1134)
    sleep(sleepyTime)


def tapPokemongoOk():
    tap(580, 1195)
    sleep(sleepyTime)


def swipeToNextPokemon():
    # TODO: Make this a bit more random
    swipe(1022, 1376, 645, 1354, 564)
    sleep(sleepyTime)


def performAppraisal():
    pressThreeLines()
    pressAppraise()
    tapSomewhereLeft()
    sleep(1.5)
    tapSomewhereLeft()


def performRename():
    tapName()
    holdBackspace()
    holdNameLine()
    tapPaste()
    tapKeyboardOk()
    tapPokemongoOk()


def getNumberOfPokemonToRename():
    while True:
        value = input('Enter the number of pokemon to rename: ')
        if value.isdigit():
            return int(value)
        print("Please enter a valid positive number")


def main():
    numberOfPokemonToRename = getNumberOfPokemonToRename()
    counter = 0
    while counter < numberOfPokemonToRename:
        performAppraisal()
        performRename()
        swipeToNextPokemon()
        print("Finshed renaming " + str(counter) + " pokemon")
        counter += 1


if __name__ == "__main__":
    main()
