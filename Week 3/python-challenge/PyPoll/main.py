import csv

import os

csvpath = os.path.join('..', 'election_data.csv')

with open(csvpath, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
    # csv_header = next(csvreader)

    for row in reader:
    	candidates.append(row[2])

    candidates =[]
    votes =[]



# candidates count?

total_votes = len(candidates)



# You will be give a set of poll data called election_data.csv. 
# The dataset is composed of three columns: Voter ID, County, 
# and Candidate. Your task is to create a Python script that 
# analyzes the votes and calculates each of the following:

# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.



# print(f'Election Results')
# print(f'-------------------------')
# print(f'Total Votes: {total_votes}')
# print(f'-------------------------')
# print(f'Khan: 
# print(f'Correy: 
# print(f'Li: 
# print(f"O'Tooley: 
# print(f'-------------------------')
# print(f'Winner: {winner_name}')
# print(f'-------------------------')