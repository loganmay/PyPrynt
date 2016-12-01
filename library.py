# # #
# This file hosts the library of functions to use in PyPrint.
# # #

# Imports
from Tkinter import *
from collections import Counter
import os
#import numpy
f = open('PrinterReport.txt', 'w')

# # # # # Pages Methods # # # # #
#### RUN BUTTON ####
def runReport(location, date, time, pages, cost, quota, maxPagesVar,
              minPagesVar, avgPagesVar, largeSmallVar, listLocationVar,
              printerUsersVar, perPrinterUsersVar, mostCostlyVar, printerCostVar,
              mostUsedDateVar, leastUsedDateVar, mostUsedTimeVar, leastUsedTimeVar):

    if maxPagesVar == 1:
        calcMaxPages(pages)
    if minPagesVar == 1:
        calcMinPages(pages)
    if avgPagesVar == 1:
        printAvg(pages)
    if largeSmallVar == 1:
        leastandMostLocation(location)
    if listLocationVar == 1:
        printListofRooms(location)
    if printerUsersVar == 1:
        printerUser(quota)
    if perPrinterUsersVar == 1:
        perPrinterUser(location, quota)
    if mostCostlyVar == 1:
        mostCostly(location, cost)
    if printerCostVar == 1:
        totalCost(location, cost)
    if mostUsedDateVar == 1:
        mostUsedDate(date)
    if leastUsedDateVar == 1:
        leastUsedDate(date)
    if mostUsedTimeVar == 1:
        mostUsedTime(date)
    if leastUsedTimeVar == 1:
        leastUsedTime(date)
    os.startfile('PrinterReport.txt')
    f.close()
#####END RUN BUTTON#######


# Calculate the max pages in a single print
def calcMaxPages(pages):
    max = 0
    for e in pages:
        if e > max:
            max = e

    # This is the output message
    message = "Max Pages: " + str(max)
    print >>f, message
    f.write(message)

# Calculate the min pages in a single print
def calcMinPages(pages):
    min = max
    for e in pages:
        if e < min:
            min = e

    # This is the ouput message
    message = "Minimum Pages: " + str(min)
    print >>f, message

# Calculate the average number of pages in all the prints
def calcAvgPages(pages):

    numEntries = len(pages)
    totalPages = sum(pages)
    average = totalPages/numEntries
    return average

# Print the average
def printAvg(pages):

    # Call calcAvgPages function to get average pages printer
    average = calcAvgPages(pages)
    # Output Message
    message = "Average number of pages printed: " + str(average)
    # Print output in new window using a label
    print >>f, message

# Calculate the standard deviation of the number of pages in the prints
def calcStdPages(pages):

    stddev = numpy.std(pages)
    return stddev

# Returns the index of the biggest print
def indexOfMaxPages(pages):

    for i,e in enumerate(pages):
        if e == calcMaxPages(pages):
            return i

# # # # # End Pages Methods # # #

# # # # # Location Methods # # # # #

# Organize the locations in an ascending order
def orderLocations(location):

    locCounter = Counter(location)
    from operator import itemgetter
    locationAscending = sorted(locCounter.items(), key=itemgetter(1), reverse=True)
    return locationAscending

# Print the most and least used locations
def leastandMostLocation(location):
    # Get organzied list
    locationAscending = orderLocations(location)

    # Print Most Used Location in the new window using a label
    mostUsed = "Most used Room: " + locationAscending[0][0]
    print >>f, mostUsed

    # Print Least Used Location in the new window using a label
    leastUsed = "Leased used Room: " + locationAscending[len(locationAscending) - 1][0]
    print >>f, leastUsed

# Print the list of rooms in ascending order according to number of prints
def printListofRooms(location):
    # Get organized list
    locationAscending = orderLocations(location)

    # Print the list to the new window my recalling a label and incrementing its position using the grid
    for key, value in locationAscending:
        message = "{} || {} prints".format(key, value)
        print >>f, message
# # # # # End Location Methods # # #

# # # # # Quota Methods # # # # #

# See if more students or professors use the printers
def printerUser(quota):
    # Initialize counts and output message
    printerUserMessage = ""
    prof = 0
    stud = 0

    # Loop through printers and count
    for e in quota:
        if e > 1000:
            prof += 1
        elif e <= 1000:
            stud += 1
    if prof > stud:
        printerUserMessage = "More Faculty use the printers."
    else:
        printerUserMessage = "More Students use the printers."

    # Print output in the new window using a label
    print >>f, printerUserMessage

# Look at professors vs. students for each printer individually
def perPrinterUser(location, quota):
    # Initialize variables
    printer = ["HPLaserJet 600 Insalaco Lab RM 20", "HPLaserJet 600 Library Left Printer", "HPLaserJet 600 Library Right Printer", "HPLaserJet 600 Passan Hall Lounge","HPLaserJet 600 Science RM 205","HPLaserJet 600 Mercy Hall RM335","HPLaserJet 600 Annex Passan Hall Lab","HPLaserJet 600 Henry Lounge","HPLaserJet 600 Mercy Hall RM349","HP Color LaserJet M651 Library"]
    perPrinterMessage = ""
    prof = 0
    stud = 0
    thisOtherIndex = 0 #this one holds the index of the printer

    # For each individual printer
    for p in printer:
        e = 0 #reset e to zero
        while (e < len(location)): #while we haven't reached the last entry in the list
            if location[e] == p: #if current entry is printer we're looking for
                if quota[e]>1000: #and if the quota is a professor's
                    prof+=1     #increment prof
                elif quota[e]<1000: #else if the quota is a student's
                    stud+=1         #increment student
            e+=1    #increment e to look at the next element

         # If more faculty use the printer
        if prof > stud:
            # Output message in new window using a label
            perPrinterMessage = "More Faculty use printer " + printer[thisOtherIndex]
            print >>f, perPrinterMessage

            #print "Prof = ", prof, " Stud = ", stud
            prof = 0
            stud = 0

        # If more students use the printer
        elif prof < stud:
            # Output message in new window using a label
            perPrinterMessage = "More students use printer " + printer[thisOtherIndex]
            print >>f, perPrinterMessage

           # print "Prof = ", prof, " Stud = ", stud
            prof = 0
            stud = 0

         # If it's a tie
        elif prof == stud:
            # Output message in new window using a label
            perPrinterMessage = "Students and Professors use printer " + printer[thisOtherIndex] + " equally"
            print >>f, perPrinterMessage

            #print "Prof = ", prof, " Stud = ", stud
            prof = 0
            stud = 0
        thisOtherIndex += 1

# Find the most costly printer and its cost
def mostCostly(location, cost):
    # Initialize variables
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

            # If the current total is greater than the max cost
            # Then update maxCost to currentCost
            if currentCost > maxCost:
                # Update maxCost to currentCost
                maxCost = currentCost

                # Set profitPrinter to the current printer
                profitPrinter = location[e - 1]

            # Reinitialize currentCost
            currentCost = 0
            # Begin next printer total
            currentCost += cost[e]

    # Message concerning the most costly printer
    mostCostlyPrinter = "The printer that is most costly:  " + profitPrinter
    # Message concerning the total most costly
    mostCostlymessage = "With a total cost of: " + str(maxCost)

    # Print most costly printer
    print >>f, mostCostlyPrinter
    print >>f, mostCostlymessage

# Find total cost for each printer
def totalCost(location, cost):
    # Initialize printer list
    printer = ["HPLaserJet 600 Insalaco Lab RM 20", "HPLaserJet 600 Library Left Printer",
               "HPLaserJet 600 Library Right Printer", "HPLaserJet 600 Passan Hall Lounge",
               "HPLaserJet 600 Science RM 205","HPLaserJet 600 Mercy Hall RM335",
               "HPLaserJet 600 Annex Passan Hall Lab","HPLaserJet 600 Henry Lounge",
               "HPLaserJet 600 Mercy Hall RM349","HP Color LaserJet M651 Library"]

    #search through each printer
    for p in printer:
        e = 0 #reset e to zero
        total = 0 # Reset e to zero

        while (e < len(location)): #while we haven't reached the last entry in the list
            if location[e] == p: #if current entry is printer we're looking for
                total += cost[e]
            e += 1
        # Outpt message
        totalCostMessage = "Printer: {:20}  ||  Total Cost: {}".format(p, total)

        # Print output into the new window using a label
        print >>f, totalCostMessage

# # # # # End Quota Methods # # #

# # # # # Search Methods # # #
def pagesSearch(location, pages, date, value, radioValue):
    # Initialize the list of printers
    printer = ["HPLaserJet 600 Insalaco Lab RM 20", "HPLaserJet 600 Library Left Printer",
               "HPLaserJet 600 Library Right Printer", "HPLaserJet 600 Passan Hall Lounge",
               "HPLaserJet 600 Science RM 205", "HPLaserJet 600 Mercy Hall RM335",
               "HPLaserJet 600 Annex Passan Hall Lab", "HPLaserJet 600 Henry Lounge",
               "HPLaserJet 600 Mercy Hall RM349", "HP Color LaserJet M651 Library"]

    # Create a new window for Output
    branch = Tk()
    branch.title("Printer Pages Search Results")
    branch.geometry("550x350")
    # Initialize variables
    numJobs = 0
    compareList = []

    # Exception Handling concerning:
    # Make sure the user entered an integer, and selected a radio button before clicking the button
    try:
        # Makes sure that the value is an integer
        value = int(value)
        # Make sure a radio button has been clicked
        if radioValue == 0:
            raise ValueError
        valid = True

    except ValueError:
        # Print a warning to the new window and set valid to false
        pageLabel = Label(branch, text="INVALID VALUE OR UNSELECTED COMPARISON\n PLEASE TRY AGAIN")
        pageLabel.pack(side=TOP)
        valid = False

    # If valid is true from above Try statement, then lets find some pages
    if valid:
        # Create a scroll bar used for the listbox
        scrollBar = Scrollbar(branch, orient=VERTICAL)

        # Create a listbox to display the jobs
        pagesList = Listbox(branch, yscrollcommand=scrollBar.set)

        # Configuring of the scrollbar and its placement on the list box
        scrollBar.config(command=pagesList.yview)
        scrollBar.pack(side=RIGHT, fill=Y)
        pagesList.pack(side=LEFT, fill=BOTH, expand=1)

        # Sequence through each printer and compare each job to the value given
        # by the user and using the comparison the user selected
        for p in printer:
            e = 0   # e loops through whole dataset, downside: Each job can be looked at multiple times
            while e < len(location): # While e isn't at the last job
                if radioValue == 1: # If radio button 1 is selected
                    if pages[e] >= value:   # compare the current value to the user value
                        if date[e] in compareList:  # if that date has already been looked at, continue with the loop
                            e += 1
                            continue
                        else:
                            compareList.append(date[e]) # Date is added to checklist
                            numJobs += 1    # Total is incremented

                            # Message is appended to the end of the listbox
                            pageMessage = "Printer: {} on {} Pages: {}".format(location[e], date[e], pages[e])
                            pagesList.insert(END, pageMessage)
                    e += 1
                if radioValue == 2: # If radio button 2 is selected
                    if pages[e] <= value: # compare the current value to the user value
                        if date[e] in compareList: # if that date has already been looked at, continue with the loop
                            e += 1
                            continue
                        else:
                            compareList.append(date[e]) # Date is added to checklist
                            numJobs += 1 # Total is incremented

                            # Message is appended to the end of the listbox
                            pageMessage = "Printer: {} on {} Pages: {}".format(location[e], date[e], pages[e])
                            pagesList.insert(END, pageMessage)
                    e += 1
                if radioValue == 3: # If radio button 3 is selected
                    if pages[e] == value: # compare the current value to the user value
                        if date[e] in compareList: # if that date has already been looked at, continue with the loop
                            e += 1
                            continue
                        else:
                            compareList.append(date[e]) # Date is added to checklist
                            numJobs += 1 # Total is incremented

                            # Message is appended to the end of the listbox
                            pageMessage = "Printer: {} on {} Pages: {}".format(location[e], date[e], pages[e])
                            pagesList.insert(END, pageMessage)
                    e += 1
        # Print the total amount of jobs on the side
        totalMessage = "{} Total Job(s)".format(numJobs)
        totalLabel = Label(branch, text=totalMessage)
        totalLabel.pack(side=TOP)

    branch.mainloop()

# # # # # Date methods # # #
def mostUsedDate(date):
    # Initialize pure lists
    pureDate = []
    pureTime = []

    # Initialize exact days
    diffDays = []

    # Initialize most used day and current most used day
    mostUsedDay = ""
    currMost = 0

    for e in range(len(date)-1):
        currentDate = date[e].split(" ")
        currentDate.pop(0)
        pureDate.append(currentDate[0])
        pureTime.append(currentDate[1])

    for e in pureDate:
        if e in diffDays:
            continue
        else:
            diffDays.append(e)
    # for e in diffDays: pagesList.insert(END, e)
    for day in diffDays:

        e = 0
        dayUsageTotal = 0   # dayUsageTotal to find the most used day

        while e < len(pureDate):
            if pureDate[e] == day:
                dayUsageTotal += 1
            e += 1

        if dayUsageTotal > currMost:
            currMost = dayUsageTotal
            mostUsedDay = day

        #print "On {}, {} jobs were printed".format(day, dayUsageTotal)
    dateMessage = "The most used date was {}\n With {} total jobs printed that day".format(mostUsedDay, currMost)
    print >>f, dateMessage

def leastUsedDate(date):
    # Initialize pure lists
    pureDate = []
    pureTime = []

    # Initialize exact days
    diffDays = []

    # Initialize most used dayad current most used day
    leastUsedDay = ""
    currLeast = 10000

    for e in range(len(date) - 1):
        currentDate = date[e].split(" ")
        currentDate.pop(0)
        pureDate.append(currentDate[0])
        pureTime.append(currentDate[1])

    for e in pureDate:
        if e in diffDays:
            continue
        else:
            diffDays.append(e)

    # for e in diffDays: pagesList.insert(END, e)
    for day in diffDays:

        e = 0
        dayUsageTotal = 0  # dayUsageTotal to find the most used day

        while e < len(pureDate):
            if pureDate[e] == day:
                dayUsageTotal += 1
            e += 1

        if dayUsageTotal < currLeast:
            currLeast = dayUsageTotal
            leastUsedDay = day

        print >>f, "On {}, {} jobs were printed".format(day, dayUsageTotal)

    dateMessage = "The least used date was {}\n With {} total jobs printed that day".format(leastUsedDay, currLeast)
    print >>f, dateMessage

def mostUsedTime(date):
    # Initialize pure lists
    pureDate = []
    pureTime = []
    pureHour = []

    # Initialize exact days
    diffHours = []

    mostUsedHour = ""
    currMost = 0

    # Split the date into pure forms
    for e in range(len(date) - 1):
        currentDate = date[e].split(" ")
        currentDate.pop(0)
        pureDate.append(currentDate[0])
        pureTime.append(currentDate[1])

    # Split the pureTime into pureHours
    for e in range(len(pureTime) - 1):
        currentTime = pureTime[e].split(":")
        pureHour.append(currentTime[0])

    # Make sure each hour is only counted once
    for e in pureHour:
        if e in diffHours:
            continue
        else:
            diffHours.append(e)

    # for e in diffHours: pagesList.insert(END, e)
    for hour in diffHours:

        e = 0
        hourUsageTotal = 0   # hourUsageTotal to find the most used hour

        while e < len(pureHour):
            if pureHour[e] == hour:
                hourUsageTotal += 1
            e += 1

        if hourUsageTotal > currMost:
            currMost = hourUsageTotal
            mostUsedHour = hour

        #print >>f, "At {}, {} jobs were printed".format(hour, hourUsageTotal)

    # if selection statement to make it easier for the user to read
    if mostUsedHour == "00":
        mostUsedHour = "12am"
    elif int(mostUsedHour) < 12:
        mostUsedHour += "am"
    else:
        regularTime = int(mostUsedHour) - 12
        mostUsedHour = str(regularTime) + "pm"

    hourMessage = "The most used hour was {}\n With {} total jobs printed during that hour".format(mostUsedHour,
                                                                                                   currMost)
    print >>f, hourMessage

def leastUsedTime(date):
    # Initialize pure lists
    pureDate = []
    pureTime = []
    pureHour = []

    # Initialize exact days
    diffHours = []

    mostUsedHour = ""
    currMost = 100000

    # Split the date into pure forms
    for e in range(len(date) - 1):
        currentDate = date[e].split(" ")
        currentDate.pop(0)
        pureDate.append(currentDate[0])
        pureTime.append(currentDate[1])

    # Split the pureTime into pureHours
    for e in range(len(pureTime) - 1):
        currentTime = pureTime[e].split(":")
        pureHour.append(currentTime[0])

    # Make sure each hour is only counted once
    for e in pureHour:
        if e in diffHours:
            continue
        else:
            diffHours.append(e)

    # for e in diffHours: pagesList.insert(END, e)
    for hour in diffHours:

        e = 0
        hourUsageTotal = 0  # hourUsageTotal to find the most used hour

        while e < len(pureHour):
            if pureHour[e] == hour:
                hourUsageTotal += 1
            e += 1

        if hourUsageTotal < currMost:
            currMost = hourUsageTotal
            mostUsedHour = hour

        #print >>f, "At {}, {} jobs were printed".format(hour, hourUsageTotal)

    # if selection statement to make it easier for the user to read
    if mostUsedHour == "00":
        mostUsedHour = "12am"
    elif int(mostUsedHour) < 12:
        mostUsedHour = str(int(mostUsedHour)) + "am"
    else:
        regularTime = int(mostUsedHour) - 12
        mostUsedHour = str(regularTime) + "pm"

    hourMessage = "The least used hour was {}\n With {} total jobs printed during that hour".format(mostUsedHour,
                                                                                                   currMost)
    print >>f, hourMessage









# # # # # High Volume Methods # # # # #
# Returns a list containing the indices of high volume prints in an array
#  (# prints > or = 1 std dev above the mean)
def highVolumeIndices(pages):

    highVolumeIndices = []
    for i,e in enumerate(pages):
        if e >= calcAvgPages(pages) + calcStdPages(pages):
            highVolumeIndices.append(i)
    return highVolumeIndices


# Returns a list of the locations of high volume print jobs
def highVolumeLocations(pages, location):

    highVolume = []
    highVolumeInds = highVolumeIndices(pages)

    for e in highVolumeInds:
        highVolume.append(location[e])
    return highVolume


# # # End High Volume Methods # # # # #

# # # Test Button Methods # # #




# # # END Test Button Methods # # #



