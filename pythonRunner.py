
from time import sleep
from CsvExtractor import CsvExtractor
from AdbInteractor import AdbInteractor as adb


class Renamer:

    def __init__(self, sleepyTime):
        self.sleepyTime = sleepyTime
        self.csvExtractor = CsvExtractor()

    def pressThreeLines(self):
        # Following line spreads the tuple returned by the extractor into x and y
        adb.tap(*self.csvExtractor.getCoordinatesFor('threeLines'))
        sleep(self.sleepyTime)

    def pressAppraise(self):
        adb.tap(*self.csvExtractor.getCoordinatesFor('appraise'))
        sleep(self.sleepyTime)

    def tapSomewhereLeft(self):
        # TODO: Make this a bit more random
        adb.tap(450, 1700)
        sleep(self.sleepyTime)

    def tapName(self):
        adb.tap(*self.csvExtractor.getCoordinatesFor('name'))
        sleep(self.sleepyTime)

    def holdBackspace(self):
        adb.hold(
            *self.csvExtractor.getCoordinatesFor('backspace'), 998)
        sleep(self.sleepyTime)

    def holdNameLine(self):
        adb.hold(
            *self.csvExtractor.getCoordinatesFor('nameLine'), 583)
        sleep(self.sleepyTime)

    def tapPaste(self):
        adb.tap(*self.csvExtractor.getCoordinatesFor('paste'))
        sleep(self.sleepyTime)

    def tapKeyboardOk(self):
        adb.tap(*self.csvExtractor.getCoordinatesFor('keyboardOk'))
        sleep(self.sleepyTime)

    def tapPokemongoOk(self):
        adb.tap(*self.csvExtractor.getCoordinatesFor('pokemongoOk'))
        sleep(self.sleepyTime)

    def swipeToNextPokemon(self):
        # TODO: Make this a bit more random
        adb.swipe(1022, 1376, 645, 1354, 564)
        sleep(self.sleepyTime)

    def performAppraisal(self):
        self.pressThreeLines()
        self.pressAppraise()
        self.tapSomewhereLeft()
        sleep(1.5)
        self.tapSomewhereLeft()

    def performRename(self):
        self.tapName()
        self.holdBackspace()
        self.holdNameLine()
        self.tapPaste()
        self.tapKeyboardOk()
        self.tapPokemongoOk()

    def getNumberOfPokemonToRename(self):
        while True:
            value = input('Enter the number of pokemon to rename: ')
            if value.isdigit():
                return int(value)
            print("Please enter a valid positive number")

    def rename(self):
        numberOfPokemonToRename = self.getNumberOfPokemonToRename()
        counter = 0
        while counter < numberOfPokemonToRename:
            self.performAppraisal()
            self.performRename()
            self.swipeToNextPokemon()
            counter += 1
            print("Finshed renaming " + str(counter) + " pokemon")


if __name__ == "__main__":
    renamer = Renamer(0.5)
    renamer.rename()
