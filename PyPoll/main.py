# PyPoll Instructions
# In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

# You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

#1. Use CSV module to load, read and clean data by making 3 vectors that contain each of the csv data.
import csv


file_name = 'PyPoll/Resources/election_data.csv'

with open(file_name, 'r') as file:
        raw_data = csv.reader(file)
        data = [line for line in raw_data]


# filter data 
ballot_ids = [row[0] for row in data if row[0]!= 'Ballot ID']
counties = [row[1] for row in data if row[1]!= 'County']
candidates = [row[2] for row in data if row[2]!= 'Candidate']

#testing code 
# print(ballot_ids[0:5])
# print(counties[0:5])
# print(candidates[0:5])

# The total number of votes cast
total_votes = len(ballot_ids)


# A complete list of candidates who received votes

list_of_candidates = [name for name in set(candidates)]


# The percentage of votes each candidate won & The total number of votes each candidate won
# Set counters for each candidates votes
ccs_total_votes = 0
rad_total_votes = 0
dd_total_votes = 0
for row in data:
        if row[2] == 'Charles Casper Stockham':
                ccs_total_votes += 1
        elif row[2] == 'Raymon Anthony Doane':
                rad_total_votes += 1
        else:
                dd_total_votes += 1
ccs_vote_perc = round((ccs_total_votes/total_votes)*100,3)
rad_vote_perc = round((rad_total_votes/total_votes)*100,3)
dd_vote_perc = round((dd_total_votes/total_votes)*100,3)


# The winner of the election based on popular vote

# Your analysis should align with the following results:

# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------


