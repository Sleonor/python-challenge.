# First we'll import the os module 
# This will allow us to create file paths across operating systems
import os
# csvpath = os.path.join('Resources', 'accounting.csv')
election1_path = 'election_data_1.csv'
election2_path = 'election_data_2.csv'

election_csv_paths = [election1_path, election2_path]


# Method 2: Improved Reading using CSV module
import csv
# election1_csvfile =  open(election1_path, newline='')

#aggregate data
count = 0
results = {}

#for each file
for path in election_csv_paths:
    #open
    csvfile = open(path)
    #make reader
    csvreader = csv.reader(csvfile)
    #skip header
    next(csvreader, None)
    #iterate through data
    for row in csvreader:
        count += 1
        #[voterid, county, candidate]
        candidate = row[2]
        if candidate not in results:
            results[candidate] = 1
        else:
            results[candidate] += 1
winner = ''
wiener_size = 0

candidates = ''
#find wiener
for candidate in results:
    votes = results[candidate]
    if votes > winner_size:
        winner = candidate
        winner_size = votes
    candidates += '%s:\t%.2f%% (%i)\n'%(candidate, votes/count*100, votes)

output = '''
Election Results
-------------------------
Total Votes: %i
%s
-------------------------
Winner: %s
-------------------------
'''%(count,candidates,wiener)

with open('output.txt', 'w') as outfile:
    outfile.write(output)
    outfile.close()

print(output)