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
welcomeLabel = Label(root, text="Welcome to PyPrint!")
welcomeLabel.grid(row=0, sticky=W)

## Partition Label
partitionLabel = Label(root, text="-------------------------Job Page Information------------------------")
partitionLabel.grid(row=1, columnspan=5, sticky=W)

# Max Pages
btnCalcMaxPages = Button(root, text="Calculate Maximum Pages Printed", command= lambda: library.calcMaxPages(pages))
btnCalcMaxPages.bind("<Button-1>")
btnCalcMaxPages.grid(row=2, column=0, sticky=W)

# Min Pages
btnCalcMinPages = Button(root, text="Calculate Minimum Pages Printed", command= lambda: library.calcMinPages(pages))
btnCalcMinPages.bind("<Button-1>")
btnCalcMinPages.grid(row=2, column=1, sticky=W)

# Avg Pages
btnCalcAvgPages = Button(root, text="Calculate Average Pages Printed", command= lambda: library.printAvg(pages))
btnCalcAvgPages.bind("<Button-1>")
btnCalcAvgPages.grid(row=3, columnspan=3)

## Partition Label
partitionLabel = Label(root, text="---------Printer Visit Information--------||--------Location Information----------")
partitionLabel.grid(row=4, columnspan=5, sticky=W)

# Least and Most Locations
btnLargeSmallLocations = Button(root, text="Most and Least Visited Printers", command= lambda: library.leastandMostLocation(location))
btnLargeSmallLocations.bind("<Button-1>")
btnLargeSmallLocations.grid(row=5, sticky=W)

# Locations and Prints
btnListLocations = Button(root, text="Print the locations and prints of all printers", command= lambda: library.printListofRooms(location))
btnListLocations.bind("<Button-1>")
btnListLocations.grid(row=5, column=1, sticky=W)

## Partition Label
partitionLabel = Label(root, text="---------------------------------Printer User Information--------------------------------")
partitionLabel.grid(row=6, columnspan=5, sticky=W)

# Students vs. Professors for all printers
btnPrinterUsers = Button(root, text="Who Uses Every Printer More", command= lambda:library.printerUser(quota))
btnPrinterUsers.bind("<Button-1>")
btnPrinterUsers.grid(row=7, sticky=W)

# Students vs. Professors per printer
btnPerPrinterUsers = Button(root, text="Who Uses Each Printer More", command= lambda:library.perPrinterUser(location, quota))
btnPerPrinterUsers.bind("<Button-1>")
btnPerPrinterUsers.grid(row=7, column=1, sticky=W)

## Partition Label
partitionLabel = Label(root, text="--------------------------------Job Cost Information-------------------------------")
partitionLabel.grid(row=8, columnspan=5, sticky=W)

# Most costly printer
btnMostCostly = Button(root, text="Most Costly Printer", command= lambda:library.mostCostly(location, cost))
btnMostCostly.bind("<Button-1>")
btnMostCostly.grid(row=9, sticky=W)

# Each Printer Cost
btnPrinterCost = Button(root, text="Each Printer Cost", command=lambda: library.totalCost(location, cost))
btnPrinterCost.bind("<Button-1>")
btnPrinterCost.grid(row=9, column=1, sticky=W)

## Partition Label
partitionLabel = Label(root, text="-----------------------Search for Job specific Information---------------------------")
partitionLabel.grid(row=10, columnspan=5, sticky=W)

# Page value search
pageEntry = Entry(root) # Entry for the value
pageEntry.grid(row=11, column=1, sticky=E)

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






''''# High Volume Prints
btnHighVolume = Button(root, text="Calculate the places where high volume prints take place", command= lambda:library.highVolumeLocations(pages, location))
btnHighVolume.bind("<Button-1>")
btnHighVolume.grid(row=9, sticky=W)'''


# Test buttons create new branch = tk()


# Run the root event handling loop
root.mainloop()

## End GUI Methods







