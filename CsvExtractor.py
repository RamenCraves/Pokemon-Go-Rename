import csv


class CsvExtractor:
    def __init__(self):
        self.coordinates = {}
        self.readCsv()

    def readCsv(self):
        with open('coordinates.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.coordinates[row[0]] = (row[1], row[2])

    def getCoordinatesFor(self, key):
        return self.coordinates[key]
