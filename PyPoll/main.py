import os
import csv

file_path = os.path.join("", "Resources", "election_data.csv")

electionData = []
electionData_length = 0
voteResults = []
candidates = []
#voteTotals = []
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

#voteTotals = [0]  *  len(candidates)
#voteResults = [0] * len(candidates)


for idx, name in enumerate(candidates):
    for index in range(electionData_length):
        if electionData[index]["Candidate"] == name:
        #    voteTotals[idx] +=1
            voteTotals += 1
    # voteResults[idx] = {"Candidate": name, "VoteTotals" : voteTotals[idx], "PercentageVotes": round((voteTotals[idx]/electionData_length)*100, 2)}
    voteResults.append({"Candidate": name, "VoteTotals" : voteTotals, "PercentageVotes": round((voteTotals/electionData_length)*100, 2)})
    voteTotals = 0

print(voteTotals)
print(voteResults)
