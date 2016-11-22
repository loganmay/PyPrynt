# # #
# This file hosts the library of functions to use in PyPrint.
# # #

# Imports
from collections import Counter
import numpy


# # # # # Pages Methods # # # # #

# Calculate the max pages in a single print
def calcMaxPages(pages):
    max = 0
    for e in pages:
        if e > max:
            max = e
    print "Max Pages: ", max


# Calculate the min pages in a single print
def calcMinPages(pages):

    min = max
    for e in pages:
        if e < min:
            min = e
    print "Min Pages: ", min


# Calculate the average number of pages in all the prints
def calcAvgPages(pages):

    numEntries = len(pages)
    totalPages = sum(pages)
    average = totalPages/numEntries
    return average


# Print the average
def printAvg(pages):
    average = calcAvgPages(pages)
    print "Average number of pages printed: ", average


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
    # Print Most Used Location
    print "Most Used Room: ", locationAscending[0][0]

    # Print Least Used Location
    print "Least Used Room: ", locationAscending[len(locationAscending ) - 1][0]
    print "\n"


# Print the list of rooms in ascending order according to number of prints
def printListofRooms(location):

    # Get organized list
    locationAscending = orderLocations(location)
    print "List of Rooms: "

    # Print the list
    for key, value in locationAscending:
        print "{} || {} prints".format(key, value)
    print " "


# # # # # End Location Methods # # #


# # # # # Quota Methods # # # # #

# See if more students or professors use the printers
def printerUser(quota):

    # Initialize counts
    prof = 0
    stud = 0

    # Loop through printers and count
    for e in quota:
        if e > 1000:
            prof += 1
        elif e <= 1000:
            stud += 1
    if prof > stud:
        print "More Faculty use the printers"
    else:
        print "More Students use the printers"


# Look at professors vs. students for each printer individually
def perPrinterUser(location, quota):

    # Initialize variables
    printer = ["HPLaserJet 600 Insalaco Lab RM 20", "HPLaserJet 600 Library Left Printer", "HPLaserJet 600 Library Right Printer", "HPLaserJet 600 Passan Hall Lounge","HPLaserJet 600 Science RM 205","HPLaserJet 600 Mercy Hall RM335","HPLaserJet 600 Annex Passan Hall Lab","HPLaserJet 600 Henry Lounge","HPLaserJet 600 Mercy Hall RM349","HP Color LaserJet M651 Library"]
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
            print "More Faculty use printer " + printer[thisOtherIndex]
            #print "Prof = ", prof, " Stud = ", stud
            prof = 0
            stud = 0

        # If more students use the printer
        elif prof < stud:
            print "More Students use printer " + printer[thisOtherIndex]
           # print "Prof = ", prof, " Stud = ", stud
            prof = 0
            stud = 0

         # If it's a tie
        elif prof == stud:
            print "Students and Professors use printer " + printer[thisOtherIndex] + " equally"
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
    print " "
    print "The printer that is most costly:  ", profitPrinter
    print "With a total cost of: ", maxCost


# # # # # End Quota Methods # # #


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
