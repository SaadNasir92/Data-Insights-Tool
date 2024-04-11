import csv

# File path declaration
file_name = 'PyPoll/Resources/election_data.csv'

# Create function to make dashes in the analysis
def make_dashes():
    print('---------------')

# Create function to make report and print to console.
def poll_analysis(csv_data):
    # Read the CSV Data.
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
                    
    # Begin Printing Analysis Data
    print("\nElection Results\n")
    make_dashes()
    
    # The total number of votes cast
    total_votes = sum(voter_data.values())
    print(f'\nTotal Votes: {total_votes}\n')
    make_dashes()

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
        print(f'\n{k}: {perc_of_votes}% ({v})\n')
    make_dashes()
    print(f'\nWinner: {winner}\n')
    make_dashes()
        
poll_analysis(file_name)
