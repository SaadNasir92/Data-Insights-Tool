import csv
import os

# File path declaration and setting the script directory. 
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'Resources', 'election_data.csv')

# Create function to make dashes in the analysis
def make_dashes():
    """
    returns string of dashes for formatting. 
    """
    return '---------------'

# Create function to make report and print to console.
def poll_analysis(path_to_csv):
    """
    Clean, manipulate and calculate based on the CSV data and returns a list of analysis lines to be further worked on.

    Args:
        csv_data files

    Returns:
        list of strings to work on further.
    """
    # Read the CSV Data.
    with open(path_to_csv, 'r') as file:
        raw_data = csv.reader(file)
        column_headers = next(raw_data)
        data = [line for line in raw_data]
        
    # Make a dictionary that stores keys as candidate names and the total # of votes they earned.
    voter_data = {}
    for row in data:
        if row[2] not in voter_data:
            voter_data[row[2]] = 1
        else:
            voter_data[row[2]] = voter_data[row[2]] + 1
                    
    # Start building the return of the function which we will use to write and create the analysis as a .txt file and print to console.
    lines_to_write = ['Election Results\n']
    create_dashes = make_dashes()
    lines_to_write.append(create_dashes)

    # The total number of votes cast
    total_votes = sum(voter_data.values())
    lines_to_write.append(f'\nTotal Votes: {total_votes}\n')
    lines_to_write.append(create_dashes)

    # A complete list of candidates who received votes. Not printing anywhere, only included per request.
    list_candidates = list(voter_data.keys())

    # The percentage of votes each candidate won & The total number of votes each candidate won
    winner_tracker = 0
    winner = ''
    for k, v in voter_data.items():
        perc_of_votes = round((v/total_votes)*100, 3)
        if perc_of_votes > winner_tracker:
            winner = k
            winner_tracker = perc_of_votes
        lines_to_write.append(f'\n{k}: {perc_of_votes}% ({v})\n')
    lines_to_write.append(create_dashes)
    lines_to_write.append(f'\nWinner: {winner}\n')
    lines_to_write.append(create_dashes)
     
    # return the lines to write list so that we can use it to make the .txt file.
    return lines_to_write

# write to the file & console
final_line_list = poll_analysis(file_path)
output_filename_path = os.path.join(script_dir, 'analysis', 'poll_analysis.txt')
with open(output_filename_path, 'w') as file:
    for line in final_line_list:
        file.write(line + '\n')
        print(line)
        