# python-challenge
This project contains two folders:  PyBank and PyPoll.  Each folder contains the analysis and resources folders. Each folder also contains a main.py file.

## PyBank  
The PyBank resources folder contains the budget_data.csv file.  Budget_data contains 86 records.  

The main.py script performs the following code:  
* Reads data from the csv file into a reader  
* Adds data from the reader into a dictionary variable  
* Loops through the data to find a running total and  differences between months, then add the differnence to the existing dictionary  
* Sorts the list of dictionaries  
* Prints the following results to the screen and writes them to a file in the analysis folder:  
    * Total months  
    * Total  
    * Average change  
    * Greatest increase in profits  
    * Greatest decrease in profits  

## PyPoll  
The PyPoll resources folder contains the election_data.csv file. Election_data.csv contains 3,521,001 records.  

The main.py file in the PyPoll folder performs the following code:  
    *Reads the file into a reader  
    *Adds data from the reader into a list of dictionaries and also create a unique list of candidates  
    *Grab the total amount of votes  
    *Loop through the candidates names then loop through the election data to calculate votes. After calculating votes, add candidate name, vote totals and percentage of votes to a list of dictionaries.  
    *Sort the list of vote results in descending order  
    *Prints the following results to the screen and writes them to a file in the analysis folder:  
        *Total votes  
        *Each candidate with their percentage of votes and vote totals  
        *Winner  