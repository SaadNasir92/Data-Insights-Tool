import csv
import os

# File path declaration
file_name = os.path.join('PyBank', 'Resources', 'budget_data.csv')

# Create function to make dashes in the analysis
def make_dashes():
    return '---------------'
        
# Create function to make report and print to console.       
def financial_analysis(csv_data):
    # Read the CSV Data.
    with open(csv_data, 'r') as file:
        raw_data = csv.reader(file)
        column_headers = next(raw_data)
        data = [line for line in raw_data]

    # Separate the dates and the p/l in to their own respectives lists.
    dates = [row[0] for row in data]
    profit_and_losses = [int(row[1]) for row in data]

    # Start building the return of the function which we will use to write and create the analysis as a .txt file and print to console.
    lines_to_write = ['Financial Analysis\n']
    create_dashes = make_dashes()
    lines_to_write.append(create_dashes)

    # Calculate total months
    total_months = len(dates)
    lines_to_write.append(f'\nTotal Months: {total_months}')
    
    # The net total amount of "Profit/Losses" over the entire period
    net_total = sum(profit_and_losses)
    lines_to_write.append(f'\nTotal: ${net_total}')
    
    # The changes in "Profit/Losses" over the entire period, and then the average of those changes
    profit_loss_delta = [(profit_and_losses[index+1] - profit_and_losses[index]) for index in range(len(profit_and_losses)) if profit_and_losses[-1] != profit_and_losses[index]]
    average_p_and_l = round(sum(profit_loss_delta)/len(profit_loss_delta), 2)
    lines_to_write.append(f'\nAverage Change: ${average_p_and_l}')

    # The greatest increase in profits (date and amount) over the entire period
    max_delta = (max(profit_loss_delta))
    max_delta_mo = dates[profit_loss_delta.index(max_delta) + 1]
    lines_to_write.append(f'\nGreatest Increase in Profits: {max_delta_mo} ({max_delta})')

    # The greatest decrease in profits (date and amount) over the entire period
    min_delta = (min(profit_loss_delta))
    min_delta_mo = dates[profit_loss_delta.index(min_delta) + 1]
    lines_to_write.append(f'\nGreatest Decrease in Profits: {min_delta_mo} ({min_delta})')
    
    # return the lines to write list so that we can use it to make the .txt file.
    return lines_to_write

# write to the file & console
final_line_list = financial_analysis(file_name)
output_filename_path = 'PyBank/analysis/financial_analysis.txt'
with open(output_filename_path, 'w') as file:
    for line in final_line_list:
        file.write(line + '\n')
        print(line)
