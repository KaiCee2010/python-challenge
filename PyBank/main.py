import os
import csv

file_path = os.path.join("", "Resources", "budget_data.csv")

monthPL = []
netPL = 0
nextIndex = 1
monthPL_length = 0
monthPL_diff = 0

with open(file_path, "r") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter = ",")
    
    for row in csvreader:
        monthPL.append(row)

#print(monthPL[1]["Profit/Losses"])
monthPL_length = len(monthPL)
#sorted(monthPL, key = lambda i: i['Profit/Losses']))
monthPL[0]["Difference"] = 0
for index in range(monthPL_length):
    netPL += (int(monthPL[index]["Profit/Losses"]))
    if nextIndex < monthPL_length:
        monthPL_diff  = (int(monthPL[nextIndex]["Profit/Losses"])) - (int(monthPL[index]["Profit/Losses"]))
        monthPL[nextIndex]["Difference"] = monthPL_diff
        print(monthPL[index])
        nextIndex += 1

print(netPL)


# numMonths = 0
# valProfitLoss = []
# netProfitLoss = 0
# netDiff = 0
# avgDiff = 0
# diff = []
# with open(file_path, "r") as csvfile:
#     csvreader = csv.reader(csvfile, delimiter = ",")
    
#     header = next(csvreader)

#     # Loop through each row and check if we can find the requested movie
#     for row in csvreader:
#         numMonths += 1
#         valProfitLoss.append(int(row[1]))
        

# valProfitListLength = len(valProfitLoss)
# print(valProfitListLength)

# nextIndex = 1
    

# for index in range(valProfitListLength):
#     netProfitLoss += valProfitLoss[index]     
#     if nextIndex < valProfitListLength:
#         print(f"Index is {valProfitLoss[index]}")
#         netDiff = netDiff + (valProfitLoss[nextIndex] - valProfitLoss[index])
       
#         print(f"Next index is {valProfitLoss[nextIndex]}")
#         nextIndex += 1    

# nextIndex -= 1
# print(f"nextIndex is {nextIndex}")   
# print(f"NetDiff is {netDiff}")

# avgDiff = netDiff / nextIndex

# print(netProfitLoss)
# print(avgDiff)       
       

