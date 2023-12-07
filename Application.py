from FileManager import FileManager

fileManager = FileManager()

def promptInt(message):
    while True:
        try:
            return int(input(message))
        except:
            print('Invalid input. Enter an integer')

def promptSelection(message, min, max):
    while True:
        try: 
            selection = int(input(message))
        except:
            print('Invalid input. Enter an integer')
            continue

        if selection >= min and selection <= max:
            return selection
        else:
            print('Invalid input. Operation not in range')

def displaySearchResult(foundRecords):
    if foundRecords != []:
        print('Found Record(s):')

        for i in range(len(foundRecords)):
            print('ID: ' + foundRecords[i][0] + ', Name: ' + foundRecords[i][1] + ', Artist: ' + foundRecords[i][2] + ', Label: ' + foundRecords[i][3])
    else:
        print('No records found')

def showMainMenu():
    operation = promptSelection('Select operation - Add record (1), Search records (2), Edit record (3), Remove record (4), Exit (5): ', 1, 5)

    if operation == 1:
        showAddMenu()
    elif operation == 2:
        showSearchMenu()
    elif operation == 3:
        showEditMenu()
    elif operation == 4:
        showRemoveMenu()
    elif operation == 5:
        quit()

def showAddMenu():
    id = promptInt('Enter ID: ')
    name = input('Enter Name: ')
    artist = input('Enter Artist: ')
    label = input('Enter Label: ')

    if fileManager.addRecord(id, name, artist, label):
        print('Record successfully added')
    else:
        print('Addition failed. Record with desired ID already exists, or an invalid ID was chosen (0 or less)')

def showSearchMenu():
    searchMethod = promptSelection('Search for records by - ID (1), Name (2), Artist (3), Label (4): ', 1, 4)
    fieldValue = input('Enter field value: ')

    foundRecords = fileManager.searchRecords(searchMethod, fieldValue)
    displaySearchResult(foundRecords)

def showEditMenu():
    id = promptInt('Enter ID of record to edit: ')
    fieldId = promptSelection('Enter field to edit - ID (1), Name (2), Artist (3), Label (4): ', 1, 4)
    newValue = input('Enter new field value: ')

    if fileManager.editRecord(id, fieldId, newValue) == False:
        print('Edit failed. Record ID does not exist')

def showRemoveMenu():
    id = promptInt('Enter ID of record to remove: ')

    if fileManager.removeRecord(id):
        print('Successfully removed record')
    else:
        print('Record ID does not exist')

while True:
    showMainMenu()
