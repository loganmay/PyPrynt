import csv

location = []
date = []
time = []
pages = []
cost = []
quota = []

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

# Max Pages
max = 0
for e in pages:
    if e > max:
        max = e
print max

#Min Pages

#Average Pages
numEntries = len(pages)
totalPages = sum(pages)
average = totalPages/numEntries
print average

#Peak Hours

#Peak Month

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





