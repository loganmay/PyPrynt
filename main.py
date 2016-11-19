# Imports
import csv
from collections import Counter

# Initlialzie Parallel Lists
location = []
date = []
time = []
pages = []
cost = []
quota = []

# Read CSV into the parallel lists
with open('data.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    i = 0
    for row in spamreader:
        location.append(row[0])
        date.append(row[2])
        time.append(row[3])
        pages.append(int(row[4]))
        cost.append(int(row[5]))
        quota.append(int(row[6]))
        i += 1

## Page Methods

# Calc and Print Max Pages
max = 0
for e in pages:
    if e > max:
        max = e
print "Max Pages: ", max

# Calc and Print Min Pages
min = max
for e in pages:
    if e < min:
        min = e
print "Min Pages: ", min

# Calc and Print Average Pages
numEntries = len(pages)
totalPages = sum(pages)
average = totalPages/numEntries
print average

## Location Methods

# Organize the locations in an ascending order
locCounter = Counter(location)
from operator import itemgetter
locCounter_ascending = sorted(locCounter.items(), key=itemgetter(1), reverse=True)

# Print Most Used Location
print "Most Used Room: ", locCounter_ascending[0][0]

# Print Least Used Location
print "Least Used Room: ", locCounter_ascending[len(locCounter_ascending ) - 1][0]
print "\n"
print "List of Rooms:"

# Print a list of locations in ascending order
for key,value in locCounter_ascending:
    print key + ": ",value, "prints"

## Quota Methods

#Prof Vs Student Usage
#nested loops where one focuses on the printer
#(whether it's the one we're focusing on or not)
# and the other on the quota
#for i in location
#if i == printer we're looking for
#then for e in quota, (see below).
#printer++?
#need a way to associate numbers with the printers
prof = 0
stud = 0

for e in quota:
    if e > 1000:
        prof += 1
    elif e <= 1000:
        stud += 1
if prof > stud:
    print "More Faculty use the printers"
else:
    print "More Students use the printers"

