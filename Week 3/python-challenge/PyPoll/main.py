import csv

import os

csvpath = os.path.join('..', 'election_data.csv')

with open(csvpath, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	csv_header = next(csvreader)
	candidates = {}

	for row in csvreader:
		if row[2] not in candidates.keys():
			candidates[row[2]] = 0
		candidates[row[2]] = candidates[row[2]] + 1


total_votes = 0

for votes in candidates.value():
	total_votes = total_votes + votes

print ("Election Resuls\n")
print ("--------------------------\n")
