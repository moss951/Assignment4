from FileManager import FileManager

fileManager = FileManager()

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
        try:
            id = int(input('Enter ID: '))
            break
        except:
            print('Invalid input. Enter an integer')

    name = input('Enter Name: ')
    artist = input('Enter Artist: ')
    label = input('Enter Label: ')

    fileManager.addRecord(id, name, artist, label)

    print('Record successfully added')

def showSearchMenu():
    return

def showEditMenu():
    return

def showRemoveMenu():
    while True:
        try:
            id = int(input('Enter ID of record to remove: '))
            break
        except:
            print('Invalid input. Enter an integer')

    fileManager.removeRecord(id)

while True:
    showMainMenu()
