from FileManager import FileManager

fileManager = FileManager()

def promptInt(message):
    while True:
        try:
            return int(input(message))
        except:
            print('Invalid input. Enter an integer')

def displaySearchResult(foundRecords):
    if foundRecords != []:
        print('Found Records:')

        for i in range(len(foundRecords)):
            print('ID: ' + foundRecords[i][0] + ', Name: ' + foundRecords[i][1] + ', Artist: ' + foundRecords[i][2] + ', Label: ' + foundRecords[i][3])
    else:
        print('No records found')

def showMainMenu():
    userInput = input('Select operation - Add record (1), Search records (2), Edit record (3), Remove record (4), Exit (5): ')

    if userInput == '1':
        showAddMenu()
    elif userInput == '2':
        showSearchMenu()
    elif userInput == '3':
        showEditMenu()
    elif userInput == '4':
        showRemoveMenu()
    elif userInput == '5':
        quit()
    else:
        print('Invalid input')

def showAddMenu():
    while True:
        id = promptInt('Enter ID: ')

        if id >= 0:
            break
        else:
            print('Invalid input. Enter an integer that is 0 or greater')

    name = input('Enter Name: ')
    artist = input('Enter Artist: ')
    label = input('Enter Label: ')

    if fileManager.addRecord(id, name, artist, label):
        print('Record successfully added')
    else:
        print('Addition failed. Record with desired ID already exists')

def showSearchMenu():
    userInput = input('Search for records by - ID (1), Name (2), Artist (3), Label (4): ')

    foundRecords = fileManager.searchRecords(userInput, input('Enter field value: '))
    displaySearchResult(foundRecords)

def showEditMenu():
    id = promptInt('Enter ID of record to edit: ')
    fieldId = input('Enter field to edit - ID (1), Name (2), Artist (3), Label (4): ')
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
