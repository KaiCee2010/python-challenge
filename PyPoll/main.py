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
        #gather a unique list of candidates, if candidate not in list add to list
        if row["Candidate"] not in candidates:
            candidates.append(row["Candidate"])

#grab the length of the list	
electionData_length = len(electionData)

#loop through the candidate names
for name in candidates:
    #loop through the election data
    for index in range(electionData_length):
        #check the name in the candidate list against the election data
        #if name equals add to the vote total for that name
        if electionData[index]["Candidate"] == name:
            voteTotals += 1
    #add all values to the vote total list as a dictionary
    voteResults.append({"Candidate": name, "VoteTotals" : voteTotals, "PercentageVotes": round((voteTotals/electionData_length) * 100, 3)})
    #reset vote totals for next name
    voteTotals = 0

#sort the voteResults list by the vote totals in descending order so highest total is first
voteResults = sorted(voteResults, key = lambda i: i["VoteTotals"], reverse = True)

#print all the results with the necessary formatting
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

#write all the results to the file with the necessary formatting
with open(outfile_path, 'w') as txtfile:
    txtfile.write("\n")
    txtfile.write("Election Results\n")
    txtfile.write(f"{dashes}\n")
    txtfile.write(f"Total Votes: {electionData_length}\n")
    txtfile.write(f"{dashes}\n")
    for value in voteResults:
        txtfile.write(f'{value["Candidate"]}: {value["PercentageVotes"]}% ({value["VoteTotals"]})')
        txtfile.write("\n")
    txtfile.write(f"{dashes}\n")
    txtfile.write(f'Winner: {voteResults[0]["Candidate"]}\n')
    txtfile.write(f"{dashes}\n")
txtfile.close()
