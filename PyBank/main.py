import os
import csv

file_path = os.path.join("", "Resources", "budget_data.csv")

monthPL = []
monthPL_sorted = []
netPL = 0
nextIndex = 1
monthPL_length = 0
monthPL_diff = 0
monthPL_diff_total = 0
monthPL_diff_avg = 0

#Read data from csv file into a reader
with open(file_path, "r") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter = ",")
    
#Add data from reader into a dictionary variable
    for row in csvreader:
        monthPL.append(row)

#Find the length of the dictionary
monthPL_length = len(monthPL)

#add zero to the first record dictionary field
monthPL[0]["Difference"] = 0

#loop through the list by index
for index in range(monthPL_length):
    #set add profit loss value to variable to create a running total
    netPL += (int(monthPL[index]["Profit/Losses"]))
    
    #check to make sure you are not at the end of the list
    if nextIndex < monthPL_length:
        
        #calculate the difference between the current value in the dictionary and the next value
        #also re-type this values before calculation
        monthPL_diff  = (int(monthPL[nextIndex]["Profit/Losses"])) - (int(monthPL[index]["Profit/Losses"]))
        
        #add this value to the dictionary using the key 'Difference'
        monthPL[nextIndex]["Difference"] = monthPL_diff

        #calculate a running total of differnces
        monthPL_diff_total = monthPL_diff_total + monthPL_diff 
        
        #iterate to next index value
        nextIndex += 1

nextIndex -= 1

#Calculate the average difference
monthPL_diff_avg = round(monthPL_diff_total / nextIndex, 2)

#sort the list and save it to a new variable
monthPL_sorted = sorted(monthPL, key = lambda i: i["Difference"], reverse=True)

#Print results to screen
print("")
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {monthPL_length}")
print(f"Total: ${netPL}")
print(f"Average Change: ${monthPL_diff_avg}")
print(f"Greatest Increase in Profits: {monthPL_sorted[0]['Date']} (${monthPL_sorted[0]['Difference']})")
print(f"Greatest Decrease in Profits: {monthPL_sorted[85]['Date']} (${monthPL_sorted[85]['Difference']})")

#write results to file
output_path = os.path.join("","analysis", "results.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write("\nFinancial Analysis\n")
    txtfile.write("-----------------------------\n\n")
    txtfile.write(f"Total Months: {monthPL_length}\n")
    txtfile.write(f"Total: ${netPL}\n")
    txtfile.write(f"Average Change: ${monthPL_diff_avg}\n")
    txtfile.write(f"Greatest Increase in Profits: {monthPL_sorted[0]['Date']} (${monthPL_sorted[0]['Difference']})\n")
    txtfile.write(f"Greatest Decrease in Profits: {monthPL_sorted[85]['Date']} (${monthPL_sorted[85]['Difference']})")

txtfile.close()


       

