# PyPoll Instructions
# In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

# You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

#1. Use CSV module to load, read and clean data.
import csv

        # Open file and remove header row.
file_name = 'PyPoll/Resources/election_data.csv'

with open(file_name, 'r') as file:
        raw_data = csv.reader(file)
        data = [line for line in raw_data]
        data.pop(0)

        # Make a dictionary that stores keys as candidate names and the total # of votes they earned.
voter_data = {}
for row in data:
        if row[2] not in voter_data:
                voter_data[row[2]] = 1
        else:
                voter_data[row[2]] = voter_data[row[2]] + 1

# The total number of votes cast
total_votes = sum(voter_data.values())

# A complete list of candidates who received votes
list_candidates = list(voter_data.keys())


# The percentage of votes each candidate won & The total number of votes each candidate won
winner_tracker = 0
winner = ''
for k, v in voter_data.items():
        perc_of_votes = round((v/total_votes)*100, 3)
        if perc_of_votes > winner_tracker:
                winner = k
                winner_tracker = perc_of_votes
        print(f'{k}: {perc_of_votes}% ({v})')
        print(winner)


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


