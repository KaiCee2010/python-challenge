import os
import csv

infile_path = os.path.join("", "Resources", "election_data.csv")
outfile_path = os.path.join("", "analysis", "results.txt")

electionData = []
voteResults = []
candidates = []
voteTotals = 0

#Read data from csv file into a reader
with open(infile_path, "r") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter = ",")
    
#Add data from reader into a dictionary variable
    for row in csvreader:
        electionData.append(row)
        if row["Candidate"] not in candidates:
            candidates.append(row["Candidate"])
	
electionData_length = len(electionData)

for name in candidates:
    for index in range(electionData_length):
        if electionData[index]["Candidate"] == name:
            voteTotals += 1
    voteResults.append({"Candidate": name, "VoteTotals" : voteTotals, "PercentageVotes": round((voteTotals/electionData_length) * 100, 3)})
    voteTotals = 0

voteResults = sorted(voteResults, key = lambda i: i["VoteTotals"], reverse = True)

dashes = "---------------------------" 
print("\n")
print("Election Results")
print(dashes)
print(f"Total Votes: {electionData_length}")
print(dashes)

for value in voteResults:
    print(f'{value["Candidate"]}: {value["PercentageVotes"]}% ({value["VoteTotals"]})')
print(dashes)
print(f'Winner: {voteResults[0]["Candidate"]}')
print(dashes)


with open(outfile_path, 'w') as txtfile:
    txtfile.write("\n")
    txtfile.write("Election Results")
    txtfile.write(dashes)
    txtfile.write(f"Total Votes: {electionData_length}")
    txtfile.write(dashes)

    for value in voteResults:
        txtfile.write(f'{value["Candidate"]}: {value["PercentageVotes"]}% ({value["VoteTotals"]})')
    txtfile.write(dashes)
    txtfile.write(f'Winner: {voteResults[0]["Candidate"]}')
    txtfile.write(dashes)