from Record import Record

dataPath = 'data.csv'
records = []

records.append(Record(98535, 'Pabio Honey', 'Radiohead', 'EMI'))

records[0].setCsvRow(0)
records[0].appendToFile(dataPath)
records[0].setLabel('hi')
records[0].updateFileRow(dataPath)