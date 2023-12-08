from FileManager import FileManager

fileManager = FileManager()

def promptInt(message): # continuously prompts the user for an integer input
    while True:
        try:
            return int(input(message))
        except:
            print('Invalid input. Enter an integer')

def promptSelection(message, min, max): # continuously prompts the user for a number that corresponds to an operation, within a certain range
    while True:
        try: # checks if input is integer
            selection = int(input(message))
        except:
            print('Invalid input. Enter an integer')
            continue

        if selection >= min and selection <= max: # checks if input is within range
            return selection
        else:
            print('Invalid input. Operation not in range')

def displaySearchResult(foundRecords): # prints a search result from a list of returned csv rows (also a list)
    if foundRecords != []: # an empty list means no rows were added to the list
        print('Found Record(s):')

        for i in range(len(foundRecords)): # prints the csv row data
            print('ID: ' + foundRecords[i][0] + ', Name: ' + foundRecords[i][1] + ', Artist: ' + foundRecords[i][2] + ', Label: ' + foundRecords[i][3])
    else:
        print('No records found')

def showMainMenu(): # shows the main menu
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

def showAddMenu(): # shows the add record menu
    id = promptInt('Enter ID: ')
    name = input('Enter Name: ')
    artist = input('Enter Artist: ')
    label = input('Enter Label: ')

    if fileManager.addRecord(id, name, artist, label): # addRecord returns true if successful, false if unsuccessful
        print('Record successfully added')
    else:
        print('Addition failed. Record with desired ID already exists, or an invalid ID was chosen (0 or less)')

def showSearchMenu(): # shows the search records menu
    searchMethod = promptSelection('Search for records by - ID (1), Name (2), Artist (3), Label (4): ', 1, 4)
    fieldValue = input('Enter field value: ') # the new desired value for a certain field, specified by a selection prompt

    foundRecords = fileManager.searchRecords(searchMethod, fieldValue) # get search result
    displaySearchResult(foundRecords)

def showEditMenu(): # shows the edit record menu
    id = promptInt('Enter ID of record to edit: ')
    fieldId = promptSelection('Enter field to edit - ID (1), Name (2), Artist (3), Label (4): ', 1, 4)
    newValue = input('Enter new field value: ') # the new desired value for a certain field, specified by a selection prompt

    if fileManager.editRecord(id, fieldId, newValue) == False: # returns false if edit was unsuccessful, which only happens when a nonexistent ID was chosen
        print('Edit failed. Record ID does not exist')

def showRemoveMenu(): # shows the remove record menu
    id = promptInt('Enter ID of record to remove: ')

    if fileManager.removeRecord(id): # returns true if successful, false if unsuccessful (which only happens when a nonexistent ID was chosen)
        print('Successfully removed record')
    else:
        print('Record ID does not exist')

while True: # main loop
    showMainMenu()
