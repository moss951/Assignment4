from Inventory import Inventory

filePath = 'data.csv'
inventory = Inventory()

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

    inventory.addRecord(id, name, artist, label, filePath)

    print('Record successfully added')

def showSearchMenu():
    return

def showEditMenu():
    return

def showRemoveMenu():
    return

while True:
    showMainMenu()
