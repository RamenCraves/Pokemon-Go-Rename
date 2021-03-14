import subprocess
import time


def executeAdbCommand(values):
    cmd = ['./adb.exe', *values]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    process.wait()


def tapOnLocation(x, y):
    executeAdbCommand(['shell', 'input', 'tap', str(x), str(y)])


def swipe(xStart, yStart, time, xEnd=-1, yEnd=-1):
    if xEnd == -1:
        xEnd = xStart

    if yEnd == -1:
        yEnd = yStart

    executeAdbCommand(['shell', 'input', 'swipe', str(
        xStart), str(yStart), str(xEnd), str(yEnd), str(time)])


def pressThreeLines():
    tapOnLocation(921, 2265)


def pressAppraise():
    tapOnLocation(955, 1871)


def tapSomewhereLeft():
    # TODO: Make this a bit more random
    tapOnLocation(450, 1700)


def tapName():
    tapOnLocation(530, 1030)


def holdBackspace():
    swipe(986, 2090, 998)


def holdNameLine():
    swipe(782, 1475, 583)


def tapPaste():
    tapOnLocation(132, 1374)


def tapKeyboardOk():
    tapOnLocation(955, 1490)


def tapPokemongoOk():
    tapOnLocation(550, 1360)


def swipeToNextPokemon():
    swipe(1022, 1376, 564, 645, 1354)


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
        pressThreeLines()
        pressAppraise()
        tapSomewhereLeft()
        time.sleep(1)
        tapSomewhereLeft()
        tapName()
        holdBackspace()
        holdNameLine()
        tapPaste()
        tapKeyboardOk()
        tapPokemongoOk()
        swipeToNextPokemon()
        counter += 1


if __name__ == "__main__":
    main()
