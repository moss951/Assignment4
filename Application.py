from Record import Record

filePath = 'data.csv'
records = []

records.append(Record(98535, 'Pabio Honey', 'Radiohead', 'EMI', len(records)))

records[0].appendToFile(filePath)
records[0].setLabel('hi')
records[0].updateFileRow(filePath)
records[0].removeFromFile(filePath)