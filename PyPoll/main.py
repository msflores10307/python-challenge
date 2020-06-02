import os
import csv

data_path = os.path.join(".", "Resources", "election_data.csv")

voter_column = []
candidates_column = []
candidates = []
with open(data_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)
    row_counter = 0
    for row in csv_reader:
        voter_column.append(row[0])
        candidates_column.append(row[2])

total_votes = len(voter_column)

# to get distinct candidates
for x in candidates_column:
    if x not in candidates:
        candidates.append(x)

results = {}
results.update( {"candidates": candidates} )
totals = []
percentages = []

for y in range(len(candidates)):
    vote_counter = 0
    for z in range(len(candidates_column)):
        if candidates_column[z] == candidates[y]:
            vote_counter = vote_counter + 1
    
    totals.append(vote_counter)
    percentages.append(vote_counter*100/total_votes)

results.update( {"totals": totals} )
results.update( {"percentages": percentages} )
result_string = ''

for a in range(len(percentages)):
    string = f"{candidates[a]} : {round(percentages[a],3)}% ({totals[a]}) \n"
    result_string = result_string+string


maxi = percentages.index(max(percentages))
winner = candidates[maxi]

output_string = f'''
Election Results
~~~~~~~~~~~~~~~~~~~~~~~~~
Total Votes : {total_votes}
~~~~~~~~~~~~~~~~~~~~~~~~~
 
{result_string}
~~~~~~~~~~~~~~~~~~~~~~~~~
The winner of the election is {winner}!
~~~~~~~~~~~~~~~~~~~~~~~~~
'''

print(output_string)

output_path = os.path.join(".", "analysis", "output.csv")

with open(output_path, "w") as outfile:
    outfile.write(output_string)