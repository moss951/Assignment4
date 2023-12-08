import csv
import os

class FileManager: # handles reading and writing to the csv file
    def __init__(self): # stores file path constants
        self._FILE_PATH = 'data.csv'
        self._TEMP_FILE_PATH = 'data_temp.csv'

    def getNumRecords(self): # get the number of rows from the file
        numRecords = 0

        with open(self._FILE_PATH, 'r') as file:
            reader = csv.reader(file)

            # count numbe of rows
            for row in reader:
                numRecords += 1

        return numRecords
    
    def getRecordById(self, id): # get a record (a row in the file) from its ID.
        with open(self._FILE_PATH, 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] == str(id): # checks if the first attribute of the row is equal to the specified ID
                    return row # returns the whole row as a list
                
        return False # returns false if no record with specified ID was found
    
    def addRecord(self, id, name, artist, label): # add a row to the file
        if id <= 0: # record IDs should be 1 or greater
            return False

        with open(self._FILE_PATH, 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] == str(id): # checks if the specified ID already belongs to a record
                    return False # ensures that each record has a unique ID

        with open(self._FILE_PATH, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([id, name, artist, label]) # append record data to file

        return True
                    
    def searchRecords(self, searchMethod, value): # search for rows in the file, given a certain field attribute as a key (either ID, name, artist, or label)
        foundRecords = [] # for storing the rows that resulted from the search

        with open(self._FILE_PATH, 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                if row[searchMethod - 1] == value: # searchMethod contains an int from 1 to 4, row attribute indexes are from 0 to 3
                    foundRecords.append(row)
                
        return foundRecords
    
    def editRecord(self, id, fieldIndex, newValue): # edit a row in the file from its ID
        record = self.getRecordById(id) # get a row from the file from its ID

        if record == False: # makes sure a row was actually chosen
            return False
        
        with open(self._FILE_PATH, 'r') as readFile, open(self._TEMP_FILE_PATH, 'w', newline='') as writeFile: # read current file and write to a temporary file
            reader = csv.reader(readFile)
            writer = csv.writer(writeFile)

            for row in reader:
                if row[0] == record[0]: # if the record ID in the row matches with the specified ID
                    if fieldIndex == 1: # change ID
                        writer.writerow([newValue, row[1], row[2], row[3]])
                    elif fieldIndex == 2: # change name
                        writer.writerow([row[0], newValue, row[2], row[3]])
                    elif fieldIndex == 3: # change artist
                        writer.writerow([row[0], row[1], newValue, row[3]])
                    elif fieldIndex == 4: # change label
                        writer.writerow([row[0], row[1], row[2], newValue])
                else:
                    writer.writerow(row) # copy the rows from the read file to the temporary file

        os.remove(self._FILE_PATH) # delete the file being read from
        os.rename(self._TEMP_FILE_PATH, self._FILE_PATH) # rename the temporary file to the current file to replace the file being read from

        return True
    
    def removeRecord(self, id): # removes a row from the file from its ID
        record = self.getRecordById(id) # get a row from the file from its ID

        if record == False: # make sure a row was actually chosen
            return False

        with open(self._FILE_PATH, 'r') as readFile, open(self._TEMP_FILE_PATH, 'w', newline='') as writeFile: # read current file and write to a temporary file
            reader = csv.reader(readFile)
            writer = csv.writer(writeFile)

            for row in reader:
                if row[0] != record[0]: # copies every row from the read file to the temporary file, excluding the row with the specified ID
                    writer.writerow(row)

        os.remove(self._FILE_PATH) # delete the file being read from
        os.rename(self._TEMP_FILE_PATH, self._FILE_PATH) # rename the temporary file to the current file to reaplce the file being read from

        return True