from Record import Record

class Inventory:
    def __init__(self):
        self._records = []
    
    def addRecord(self, id, name, artist, label, filePath):
        self._records.append(Record(id, name, artist, label, len(self._records)))
        self.addRecordToFile(len(self._records) - 1, filePath)

    def addRecordToFile(self, index, filePath):
        self._records[index].appendToFile(filePath)

    def searchRecordsById(self):
        return