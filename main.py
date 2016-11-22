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
root.geometry("500x500")

# Welcome Label
welcomeLabel = Label(root, text="Welcome to PyPrint!")
welcomeLabel.grid(row=0, sticky=W)

# Max Pages
btnCalcMaxPages = Button(root, text="Calculate Max pages", command= lambda: library.calcMaxPages(pages))
btnCalcMaxPages.bind("<Button-1>")
btnCalcMaxPages.grid(row=1, sticky=W)

# Min Pages
btnCalcMinPages = Button(root, text="Calculate Min pages", command= lambda: library.calcMinPages(pages))
btnCalcMinPages.bind("<Button-1>")
btnCalcMinPages.grid(row=2, sticky=W)

# Avg Pages
btnCalcAvgPages = Button(root, text="Calculate average number of pages printed",command= lambda: library.printAvg(pages))
btnCalcAvgPages.bind("<Button-1>")
btnCalcAvgPages.grid(row=3, sticky=W)

# Least and Most Locations
btnLargeSmallLocations = Button(root, text="Calculate the most and least most visited printers", command= lambda: library.leastandMostLocation(location))
btnLargeSmallLocations.bind("<Button-1>")
btnLargeSmallLocations.grid(row=4, sticky=W)

# Locations and Prints
btnListLocations = Button(root, text="Print the locations and prints of all printers", command= lambda: library.printListofRooms(location))
btnListLocations.bind("<Button-1>")
btnListLocations.grid(row=5, sticky=W)

# Students vs. Professors for all printers
btnPrinterUsers = Button(root, text="Calculate who uses all the printers more (Students or Professors)", command= lambda:library.printerUser(quota))
btnPrinterUsers.bind("<Button-1>")
btnPrinterUsers.grid(row=6, sticky=W)

# Students vs. Professors per printer
btnPerPrinterUsers = Button(root, text="Calculate who uses each printer more (Students or Professors)", command= lambda:library.perPrinterUser(location, quota))
btnPerPrinterUsers.bind("<Button-1>")
btnPerPrinterUsers.grid(row=7, sticky=W)

# Most costly printer
btnMostCostly = Button(root, text="Calculate the most costly printer for the users", command= lambda:library.mostCostly(location, cost))
btnMostCostly.bind("<Button-1>")
btnMostCostly.grid(row=8, sticky=W)

''''# High Volume Prints
btnHighVolume = Button(root, text="Calculate the places where high volume prints take place", command= lambda:library.highVolumeLocations(pages, location))
btnHighVolume.bind("<Button-1>")
btnHighVolume.grid(row=9, sticky=W)'''

# Run the event handling loop
root.mainloop()

## End GUI Methods







