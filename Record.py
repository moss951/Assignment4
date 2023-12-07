import csv

class Record:
    def __init__(self, id, name, artist, label, row=None):
        self._id = id
        self._name = name
        self._artist = artist
        self._label = label
        self._row = row

    def getId(self):
        return self._id
    
    def getName(self):
        return self._name
    
    def getArtist(self):
        return self._artist
    
    def getLabel(self):
        return self._label

    def setId(self, id):
        self._id = id

    def setName(self, name):
        self._name = name

    def setArtist(self, artist):
        self._artist = artist

    def setLabel(self, label):
        self._label = label

    def setCsvRow(self, row):
        self._row = row

    def appendToFile(self, filePath):
        with open(filePath, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self._id, self._name, self._artist, self._label])

    def updateFileRow(self, filePath):
        fileData = []

        with open(filePath, 'r', newline='') as file:
            reader = csv.reader(file)
            fileData.extend(reader)

        with open(filePath, 'w', newline='') as file:
            writer = csv.writer(file)
            
            for i, row in enumerate(fileData):
                if i == self._row:
                    writer.writerow([self._id, self._name, self._artist, self._label])
                else:
                    writer.writerow(row)

            