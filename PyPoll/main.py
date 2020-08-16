import os
import csv

file_path = os.path.join("", "Resources", "election_data.csv")

monthPL = []
monthPL_sorted = []
netPL = 0
nextIndex = 1
monthPL_length = 0
monthPL_diff = 0
monthPL_diff_total = 0
monthPL_diff_avg = 0

electionData = []
electionData_length = 0

voteCount_Khan = 0
voteCount_Correy = 0
voteCount_Li = 0
voteCount_Otooley = 0

#Read data from csv file into a reader
with open(file_path, "r") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter = ",")
    
#Add data from reader into a dictionary variable
    for row in csvreader:
        electionData.append(row)

electionData_length = len(electionData)
print(electionData_length)
        
