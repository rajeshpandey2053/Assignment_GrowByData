import csv
import re
with open('innob.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        p = re.compile(r'.+\/\/|www.|\..+')
        result = p.sub("", row[1])
        print(row[1], "   ", result)
