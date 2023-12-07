import csv
import os

class FileManager:
    def __init__(self):
        self._FILE_PATH = 'data.csv'
        self._TEMP_FILE_PATH = 'data_temp.csv'

    def getNumRecords(self):
        numRecords = 0

        with open(self._FILE_PATH, 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                numRecords += 1

        return numRecords
    
    def addRecord(self, id, name, artist, label):
        with open(self._FILE_PATH, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([id, name, artist, label])

    def getRecordById(self, id):
        with open(self._FILE_PATH, 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] == str(id):
                    return row
                
        return False

    def searchRecordsByName(self, name):
        foundRecords = []

        with open(self._FILE_PATH, 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                if row[1] == name:
                    foundRecords.append(row)

        return foundRecords
    
    def searchRecordsByArtist(self, artist):
        foundRecords = []

        with open(self._FILE_PATH, 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                if row[2] == artist:
                    foundRecords.append(row)

        return foundRecords
    
    def searchRecordsByLabel(self, label):
        foundRecords = []

        with open(self._FILE_PATH, 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                if row[3] == label:
                    foundRecords.append(row)

        return foundRecords
    
    def editRecord(self, id, fieldIndex):
        return
    
    def removeRecord(self, id):
        record = self.getRecordById(id)

        with open(self._FILE_PATH, 'r') as readFile, open(self._TEMP_FILE_PATH, 'w', newline='') as writeFile:
            reader = csv.reader(readFile)
            writer = csv.writer(writeFile)

            for row in reader:
                if row[0] != record[0]:
                    writer.writerow(row)

        os.remove(self._FILE_PATH)
        os.rename(self._TEMP_FILE_PATH, self._FILE_PATH)