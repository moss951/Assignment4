import csv

class FileManager:
    def __init__(self):
        self._FILE_PATH = 'data.csv'

    def getNumRecords(self):
        numRecords = 0

        with open(self._FILE_PATH, 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                numRecords += 1

        return numRecords

    def getRecordById(self, id):
        with open(self._FILE_PATH, 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] == str(id):
                    return row
                
        return False
    
    def addRecord(self, id, name, artist, label):
        with open(self._FILE_PATH, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([id, name, artist, label])

    def removeRecord(self, id):
        record = self.getRecordById(id)

        with open(self._FILE_PATH, 'r+', newline='') as file:
            reader = csv.reader(file)
            writer = csv.writer(file)
            
            for row in reader:
                if row[0] != record[0]:
                    writer.writerow(row)
    
    def searchRecordsByArtist(self):
        return
    
    def searchRecordsByLabel(self):
        return