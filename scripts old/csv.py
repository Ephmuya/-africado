import csv
import json

csvFilePath = './complience.csv'
jsonFilePath = './farmer.json'

def farmerData():
    arr = []
    # read the csv and add the arr to a array
    with open(csvFilePath) as csvFile:
        csvReader = csv.DictReader(csvFile)
        print(csvReader)
        for csvRow in csvReader:
            arr.append(csvRow)
    farmer = json.dumps(arr, indent=4)
    print(farmer)
    return farmer

farmerData()