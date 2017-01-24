#open file products.csv, run through and print line by line

import csv
with open('products.csv', 'r') as csvfile:
    lineReader = csv.reader(csvfile, delimiter=',')
    next(lineReader , None)  # skip the headers
    for row in lineReader:

            #print entire line|ROW
            print(row)

            #print a column
            print(row[0])