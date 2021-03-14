import subprocess
from time import sleep


class AdbInteractor:

    @staticmethod
    def executeAdbCommand(values):
        cmd = ['./adb.exe', *values]
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        process.wait()

    @staticmethod
    def tap(x, y):
        AdbInteractor.executeAdbCommand(
            ['shell', 'input', 'tap', str(x), str(y)])

    @staticmethod
    def swipe(xStart, yStart, xEnd, yEnd, time):
        AdbInteractor.executeAdbCommand(['shell', 'input', 'swipe', str(
            xStart), str(yStart), str(xEnd), str(yEnd), str(time)])

    @staticmethod
    def hold(x, y, time):
        AdbInteractor.executeAdbCommand(['shell', 'input', 'swipe', str(
            x), str(y), str(x), str(y), str(time)])
