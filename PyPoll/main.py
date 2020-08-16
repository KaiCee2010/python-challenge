import os
import csv

file_path = os.path.join("", "Resources", "election_data.csv")

electionData = []
electionData_length = 0
voteResults = []
candidates = []
voteTotals = []
voteCount_Khan = 0
voteCount_Correy = 0
voteCount_Li = 0
voteCount_Otooley = 0
counter = 0
results = []
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

print(candidates)

voteTotals = [0]  *  len(candidates)
results = [0] * len(candidates)
print(voteTotals)


for idx, name in enumerate(candidates):
    for index in range(electionData_length):
        if electionData[index]["Candidate"] == name:
            voteTotals[idx] +=1
    results[idx] = {"Candidate": name, "VoteTototals" : voteTotals[idx]}


print(voteTotals)
print(results)

# for index in range(electionData_length):
#     if electionData[index]["Candidate"] == "Khan":
#     	voteCount_Khan += 1

    # elif electionData[index]["Candidate"] == "Correy":
    # 	voteCount_Correy += 1
    # elif electionData[index]["Candidate"] == "Li":
    #     voteCount_Li += 1
    # else:
    # 	voteCount_Otooley += 1

# voteResults = [
#     {"Candidate": "Khan", "Vote Count": voteCount_Khan },
#     {"Candidate": "Correy", "Vote Count": voteCount_Correy },
#     {"Candidate": "Li", "Vote Count": voteCount_Li },
#     {"Candidate": "O'Tooley", "Vote Count": voteCount_Otooley },
# ]


# print(voteCount_Khan)
# print(voteCount_Correy)
# print(voteCount_Li)
# print(voteCount_Otooley)

# print(voteResults)