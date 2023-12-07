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
        with open(self._FILE_PATH, 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] == str(id):
                    return False

        with open(self._FILE_PATH, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([id, name, artist, label])

        return True

    def getRecordById(self, id):
        with open(self._FILE_PATH, 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] == str(id):
                    return row
                
        return False
                    
    def searchRecords(self, field, value):
        foundRecords = []

        with open(self._FILE_PATH, 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                if field == '1':
                    if row[0] == str(value):
                        foundRecords.append(row)
                        break
                elif field == '2':
                    if row[1] == value:
                        foundRecords.append(row)
                elif field == '3':
                    if row[2] == value:
                        foundRecords.append(row)
                elif field == '4':
                    if row[3] == value:
                        foundRecords.append(row)
                
        return foundRecords
    
    def editRecord(self, id, fieldIndex, newValue):
        record = self.getRecordById(id)

        if record == False:
            return False
        
        with open(self._FILE_PATH, 'r') as readFile, open(self._TEMP_FILE_PATH, 'w', newline='') as writeFile:
            reader = csv.reader(readFile)
            writer = csv.writer(writeFile)

            for row in reader:
                if row[0] == record[0]:
                    if fieldIndex == '1':
                        writer.writerow([newValue, row[1], row[2], row[3]])
                    elif fieldIndex == '2':
                        writer.writerow([row[0], newValue, row[2], row[3]])
                    elif fieldIndex == '3':
                        writer.writerow([row[0], row[1], newValue, row[3]])
                    elif fieldIndex == '4':
                        writer.writerow([row[0], row[1], row[2], newValue])
                    else:
                        return False
                else:
                    writer.writerow(row)

        os.remove(self._FILE_PATH)
        os.rename(self._TEMP_FILE_PATH, self._FILE_PATH)

        return True
    
    def removeRecord(self, id):
        record = self.getRecordById(id)

        if record == False:
            return False

        with open(self._FILE_PATH, 'r') as readFile, open(self._TEMP_FILE_PATH, 'w', newline='') as writeFile:
            reader = csv.reader(readFile)
            writer = csv.writer(writeFile)

            for row in reader:
                if row[0] != record[0]:
                    writer.writerow(row)

        os.remove(self._FILE_PATH)
        os.rename(self._TEMP_FILE_PATH, self._FILE_PATH)

        return True