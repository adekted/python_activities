import os
import csv

csvpath = os.path.join('.',"cereal.csv")

with open(csvpath, newline = '') as csvfile:
    print()
    csvreader = csv.reader(csvfile, delimiter = ",")
    for row in csvreader:
        if float(row[7]) >= 5:
            print(row[0] + " --- " + row[7])
    print()