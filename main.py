## Imports
import csv
from Tkinter import *
import library


## Initlialize Parallel Lists
location = []
date = []
time = []
pages = []
cost = []
quota = []
titleLine = []

## Read CSV data into the parallel lists
with open('data.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    i = 0

    for row in spamreader:
        if len(titleLine) < 1:
            titleLine.append(row)
            titleLine = titleLine[0] # fixes formatting
        else:
            location.append(row[0])
            date.append(row[2])
            time.append(row[3])
            pages.append(int(row[4]))
            cost.append(int(row[5]))
            quota.append(int(row[6]))
            i += 1

## GUI Methods

# Create root Tk() object and set values
root = Tk()
root.title("PyPrint")
root.geometry("600x500")

# Welcome Label
welcomeLabel = Label(root, text="Select the options you wish to print:")
welcomeLabel.grid(row=0, sticky=W)

## Partition Label
partitionLabel = Label(root, text="Job Page Information", font=("Helvetica", 12))
partitionLabel.grid(row=1, columnspan=5, sticky=W, padx=5)

# Max Pages
maxPagesVar = IntVar()
checkCalcMaxPages= Checkbutton(root, text="Maximum pages in a single print", variable=maxPagesVar).grid(row=2, column=0, sticky=W, padx=25)
#library.calcMaxPages(pages))

# Min Pages
minPagesVar = IntVar()
checkCalcMinPages = Checkbutton(root, text="Minimum pages in a single print", variable=minPagesVar).grid(row=3, column=0, sticky=W, padx=25)
# library.calcMinPages(pages)

# Avg Pages
avgPagesVar = IntVar()
checkCalcAvgPages = Checkbutton(root, text="Calculate Average Pages Printed", variable=avgPagesVar).grid(row=4, column=0, sticky=W, padx=25)
# library.printAvg(pages)

## Partition Label
partitionLabel = Label(root, text="Printer Visit Information", font=("Helvetica", 12))
partitionLabel.grid(row=5, columnspan=5, rowspan=3, sticky=W, padx=5)

# Least and Most Locations
largeSmallVar = IntVar()
checkLargeSmallLocations = Checkbutton(root, text="Calculate Most and Least Visited Printers", variable=largeSmallVar).grid(row=8, column=0, sticky=W, padx=25)
# library.leastandMostLocation(location))

## Partition Label
partitionLabel = Label(root, text="Location Information", font=("Helvetica", 12))
partitionLabel.grid(row=9, columnspan=5, rowspan=3, sticky=W, padx=5)

# Locations and Prints
listLocationVar = IntVar()
checkListLocations = Checkbutton(root, text="Print the locations and prints of all printers", variable=listLocationVar).grid(row=12, column=0, sticky=W, padx=25)
# library.printListofRooms(location))

## Partition Label
partitionLabel = Label(root, text="Printer User Information", font=("Helvetica", 12))
partitionLabel.grid(row=13, columnspan=5, rowspan=3, sticky=W, padx=5)

# Students vs. Professors for all printers
printerUsersVar = IntVar()
checkPrinterUsers = Checkbutton(root, text="Who Uses Every Printer More", variable=printerUsersVar).grid(row=16, column=0, sticky=W, padx=25)
# library.printerUser(quota)

# Students vs. Professors per printer
perPrinterUsersVar = IntVar()
checkPerPrinterUsers = Checkbutton(root, text="Who Uses Each Printer More", variable=perPrinterUsersVar).grid(row=17, column=0, sticky=W, padx=25)
#library.perPrinterUser(location, quota)

## Partition Label
partitionLabel = Label(root, text="Job Cost Information", font=("Helvetica", 12))
partitionLabel.grid(row=18, columnspan=5, rowspan=3, sticky=W, padx=5)

# Most costly printer
mostCostlyVar = IntVar()
checkMostCostly = Checkbutton(root, text="Most Costly Printer", variable=mostCostlyVar).grid(row=21, column=0, sticky=W, padx=25)

# Each Printer Cost
printerCostVar = IntVar()
checkPrinterCost = Checkbutton(root, text="Each Printer Cost", variable=printerCostVar).grid(row=22, column=0, sticky=W, padx=25)
# library.totalCost(location, cost))

## Partition Label
partitionLabel = Label(root, text="Job Date and Time Information", font=("Helvetica", 12))
partitionLabel.grid(row=23, columnspan=5, rowspan=3, sticky=W, padx=5)

# Most Used Date
mostUsedDateVar = IntVar()
checkMostUsedDate = Checkbutton(root, text="Most used Date", variable=mostUsedDateVar).grid(row=26, column=0, sticky=W, padx=25)

# Least Used Date
leastUsedDateVar = IntVar()
checkLeastUsedDate = Checkbutton(root, text="Least used Date", variable=leastUsedDateVar).grid(row=27, column=0, sticky=W, padx=25)

# Most Used Date
mostUsedTimeVar = IntVar()
checkMostUsedTime = Checkbutton(root, text="Most used Time", variable=mostUsedTimeVar).grid(row=26, column=0, sticky=E, padx=25)

# Most Used Date
leastUsedTimeVar = IntVar()
checkLeastUsedTime = Checkbutton(root, text="Least used Time", variable=leastUsedTimeVar).grid(row=27, column=0, sticky=E, padx=25)





# Run Report                                                                # All lists and check button values passed
                                                                            # to runReport function
btnRun = Button(root, text="Run Report", command = lambda: library.runReport(location,
                                                                             date,
                                                                             time,
                                                                             pages,
                                                                             cost,
                                                                             quota,
                                                                             maxPagesVar.get(),
                                                                             minPagesVar.get(),
                                                                             avgPagesVar.get(),
                                                                             largeSmallVar.get(),
                                                                             listLocationVar.get(),
                                                                             printerUsersVar.get(),
                                                                             perPrinterUsersVar.get(),
                                                                             mostCostlyVar.get(),
                                                                             printerCostVar.get(),
                                                                             mostUsedDateVar.get(),
                                                                             leastUsedDateVar.get(),
                                                                             mostUsedTimeVar.get(),
                                                                             leastUsedTimeVar.get()))
btnRun.bind("<Button-1>")
btnRun.grid(row=29, columnspan=5, sticky=E)

'''
## Partition Label
partitionLabel = Label(root, text="Search for Job specific Information", font=("Helvetica", 12))
partitionLabel.grid(row=23, columnspan=5, rowspan=3, sticky=W, padx=5)

# Page value search
pageEntry = Entry(root) # Entry for the value
pageEntry.grid(row=13, column=1, sticky=E)

pageLabel = Label(root, text="Enter the Value")
pageLabel.grid(row=11, column=1, sticky=W)

btnPageSearch = Button(root, text="Search Jobs for Page value", command=lambda: library.pagesSearch(location,
                                                                                                    pages,
                                                                                                    date,
                                                                                                    pageEntry.get(),
                                                                                                    someV.get()))
btnPageSearch.bind("<Button-1>")
btnPageSearch.grid(row=11, sticky=W)

# The variable the radio buttons are related via
someV = IntVar()
# Print text directing the user to select a radio button
radioLabel = Label(root, text="Select how you would like to compare the value to the jobs: ").grid(row=12,
                                                                                                   column=0,
                                                                                                   sticky=W)
# The radio buttons
greaterRadio = Radiobutton(root, text="> or =", variable=someV, value=1).grid(row=12, column=1, sticky=W)
lesserRadio = Radiobutton(root, text="< or =", variable=someV, value=2).grid(row=12, column=1, sticky=N)
equalRadio = Radiobutton(root, text="=", variable=someV, value=3).grid(row=12, column=1, sticky=E)

# Test buttons create new branch = tk()
'''
# Run the root event handling loop
root.mainloop()

## End GUI Methods







