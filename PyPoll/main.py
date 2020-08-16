import os
import csv

file_path = os.path.join("", "Resources", "election_data.csv")

electionData = []
electionData_length = 0
voteResults = []
candidates = []
voteTotals = 0

#Read data from csv file into a reader
with open(file_path, "r") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter = ",")
    
#Add data from reader into a dictionary variable
    for row in csvreader:
        electionData.append(row)
        if row["Candidate"] not in candidates:
            candidates.append(row["Candidate"])
	
electionData_length = len(electionData)
print(electionData_length)


for idx, name in enumerate(candidates):
    for index in range(electionData_length):
        if electionData[index]["Candidate"] == name:
            voteTotals += 1
    voteResults.append({"Candidate": name, "VoteTotals" : voteTotals, "PercentageVotes": round((voteTotals/electionData_length)*100, 3)})
    voteTotals = 0

print(voteTotals)
print(voteResults)
