from FileManager import FileManager

fileManager = FileManager()

def promptInt(message):
    while True:
        try:
            return int(input(message))
        except:
            print('Invalid input. Enter an integer')

def displaySearchResult(foundRecords):
    if foundRecords == []:
        print('No record with this ID was found')
    else:
        print('Found Records:')

        for i in range(len(foundRecords)):
            print('ID: ' + foundRecords[i][0] + ', Name: ' + foundRecords[i][1] + ', Artist: ' + foundRecords[i][2] + ', Label: ' + foundRecords[i][3])

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
    id = promptInt('Enter ID: ')
    name = input('Enter Name: ')
    artist = input('Enter Artist: ')
    label = input('Enter Label: ')

    fileManager.addRecord(id, name, artist, label)

    print('Record successfully added')

def showSearchMenu():
    userInput = input('Search for records by - ID (1), Name (2), Artist (3), Label (4), Exit (5): ')

    if userInput == '1':
        id = promptInt('Enter ID: ')
        foundRecord = fileManager.getRecordById(id)

        print('ID: ' + foundRecord[0] + ', Name: ' + foundRecord[1] + ', Artist: ' + foundRecord[2] + ', Label: ' + foundRecord[3])
    elif userInput == '2':
        foundRecords = fileManager.searchRecordsByName(input('Enter name: '))
        displaySearchResult(foundRecords)
    elif userInput == '3':
        foundRecords = fileManager.searchRecordsByArtist(input('Enter artist: '))
        displaySearchResult(foundRecords)
    elif userInput == '4':
        foundRecords = fileManager.searchRecordsByLabel(input('Enter label: '))
        displaySearchResult(foundRecords)
    elif userInput == '5':
        return
    else:
        print('Invalid input')

def showEditMenu():
    return

def showRemoveMenu():
    id = promptInt('Enter ID of record to remove: ')
    fileManager.removeRecord(id)

while True:
    showMainMenu()
