import csv

with open("titanic.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')


    # print(list(readCSV))
    # for row in list(readCSV):
    #     print(row)
    for row in readCSV:
        print(row)