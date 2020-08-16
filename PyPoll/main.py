import os
import csv

file_path = os.path.join("", "Resources", "election_data.csv")

electionData = []
electionData_length = 0
voteResults = []
candidates = []
voteTotals = []

#Read data from csv file into a reader
with open(file_path, "r") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter = ",")
    
#Add data from reader into a dictionary variable
    for row in csvreader:
        electionData.append(row)

electionData_length = len(electionData)
print(electionData_length)

for index in range(electionData_length):
    if electionData[index]["Candidate"] not in candidates:
        candidates.append(electionData[index]["Candidate"])

voteTotals = [0]  *  len(candidates)
voteResults = [0] * len(candidates)


for idx, name in enumerate(candidates):
    for index in range(electionData_length):
        if electionData[index]["Candidate"] == name:
            voteTotals[idx] +=1
    voteResults[idx] = {"Candidate": name, "VoteTototals" : voteTotals[idx]}


print(voteTotals)
print(voteResults)
