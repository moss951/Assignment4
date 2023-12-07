import csv

class Record:
    def __init__(self, id, name, artist, label):
        self._id = id
        self._name = name
        self._artist = artist
        self._label = label

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

    def appendToFile(self, filePath):
        with open(filePath, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self._id, self._name, self._artist, self._label])