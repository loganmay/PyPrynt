# Imports
import csv
from collections import Counter
from Tkinter import *

# Initlialzie Parallel Lists
location = []
date = []
time = []
pages = []
cost = []
quota = []

# Initialize title line list
titleLine = []

# Read CSV into the parallel lists
with open('data1.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    i = 0

    for row in spamreader:
        if len(titleLine) < 1:
            titleLine.append(row)
        else:
            location.append(row[0])
            date.append(row[2])
            time.append(row[3])
            pages.append(int(row[4]))
            cost.append(int(row[5]))
            quota.append(int(row[6]))
            i += 1
# Because the row is entered as on entry in the list,
# The line below recreates the list with the entries only
titleLine = titleLine[0]

## Page Methods
def calcMaxPages(event):
    # Calc and Print Max Pages
    max = 0
    for e in pages:
        if e > max:
            max = e
    print "Max Pages: ", max
def calcMinPages(event):
    # Calc and Print Min Pages
    min = max
    for e in pages:
        if e < min:
            min = e
    print "Min Pages: ", min

# Calc and Print Average Pages
def avgPagesPrinted(event):
    numEntries = len(pages)
    totalPages = sum(pages)
    average = totalPages/numEntries
    print "The average number of pages printed is: ", average

## Location Methods
# Organize the locations in an ascending order
locCounter = Counter(location)
from operator import itemgetter
locCounter_ascending = sorted(locCounter.items(), key=itemgetter(1), reverse=True)

def leastandMostLocation(event):
    # Print Most Used Location
    print "Most Used Room: ", locCounter_ascending[0][0]

    # Print Least Used Location
    print "Least Used Room: ", locCounter_ascending[len(locCounter_ascending ) - 1][0]
    print "\n"

def printListofRooms(event):
    print "List of Rooms: "

    # Print a list of locations in ascending order
    for key, value in locCounter_ascending:
        print "{} || {} prints".format(key, value)
    print " "
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

def printerUser(event):
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

# Function mostCostly finds the most costly printer and returns the location
#  and total cost of that printer
def mostCostly(event):
    maxCost = 0
    currentCost = 0
    currPrinter = location[0]
    profitPrinter = ""
    # Cycle through every entry in location list
    for e in range(len(location)):
        # If the location entry (e) is the same as the one before(or the first),
        # Add the cost from that job to currentCost
        if location[e] == location[e - 1] or e == 0:
            currentCost += cost[e]

        # Else (so if location[e] != location[e-1]) Then we must compare the currentCost to the max cost
        else:
            # Print the Total cost for each printer
            #print "The total cost for {} is:     {}".format(location[e - 1], currentCost)

            # If the current total is greater than the max cost
            # Then update maxCost to currentCost
            if currentCost > maxCost:
                maxCost = currentCost

                # Set profitPrinter to the current printer
                profitPrinter = location[e - 1]

            # Reinitialize currentCost
            currentCost = 0
            # Begin next printer total
            currentCost += cost[e]
    print " "
    print "The printer that is most costly:  ", profitPrinter
    print "With a total cost of: ", maxCost

root = Tk()
root.title("PyPrint")
root.geometry("500x500")

welcomeLabel = Label(root, text="Welcome to PyPrint!")
welcomeLabel.grid(row=0, sticky=W)

btnCalcMaxMinPages = Button(root, text="Calculate Max and Min pages printed at once")
btnCalcMaxMinPages.bind("<Button-1>", calcMaxPages)
btnCalcMaxMinPages.bind("<Button-3>", calcMinPages)
btnCalcMaxMinPages.grid(row=1, sticky=W)

btnCalcAvgPages = Button(root, text="Calculate average number of pages printed")
btnCalcAvgPages.bind("<Button-1>", avgPagesPrinted)
btnCalcAvgPages.grid(row=2, sticky=W)

btnLargeSmallLocations = Button(root, text="Calculate the most and least most visited printers")
btnLargeSmallLocations.bind("<Button-1>", leastandMostLocation)
btnLargeSmallLocations.grid(row=3, sticky=W)

btnListLocations = Button(root, text="Print the locations and prints of all printers")
btnListLocations.bind("<Button-1>", printListofRooms)
btnListLocations.grid(row=4, sticky=W)

btnPrinterUsers = Button(root, text="Calculate who uses printer more(Students or Professors)")
btnPrinterUsers.bind("<Button-1>", printerUser)
btnPrinterUsers.grid(row=5, sticky=W)

btnMostCostly = Button(root, text="Calculate the most costly printer for the users")
btnMostCostly.bind("<Button-1>", mostCostly)
btnMostCostly.grid(row=6, sticky=W)

'''
I figure with the GUI we can implement more things such as:
An option for a user to search entries that are greater than a certain number
An option for the user to select multiple printers and maybe compare there prints or something?
Maybe an option to see when a printer is most heavily used during the day, or which date it was used the most

If you already have something set up feel free to use that jsut let me know!
Thanks guys, sorry I couldn't come tonight...
-Rob
'''

root.mainloop()







