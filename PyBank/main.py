import csv

# File path declaration
file_name = 'PyBank/Resources/budget_data.csv'

# Create function to make dashes in the analysis
def make_dashes():
    print('---------------')
        
# Create function to make report and print to console.       
def financial_analysis(csv_data):
    # Read the CSV Data.
    with open(csv_data, 'r') as file:
        raw_data = csv.reader(file)
        data = [line for line in raw_data]

    # Separate the dates and the p/l in to their own respectives lists.
    dates = [row[0] for row in data if row[0]!= 'Date']
    profit_and_losses = [int(row[1]) for row in data if row[1]!= 'Profit/Losses']

    # Start Printing Analysis
    print("\nFinancial Analysis\n")
    make_dashes()

    # Calculate total months
    total_months = len(dates)
    print(f'\nTotal Months: {total_months}')

    # The net total amount of "Profit/Losses" over the entire period
    net_total = sum(profit_and_losses)
    print(f'\nTotal: ${net_total}')

    # The changes in "Profit/Losses" over the entire period, and then the average of those changes
    profit_loss_delta = [(profit_and_losses[index+1] - profit_and_losses[index]) for index in range(len(profit_and_losses)) if profit_and_losses[-1] != profit_and_losses[index]]
    average_p_and_l = round(sum(profit_loss_delta)/len(profit_loss_delta), 2)
    print(f'\nAverage Change: ${average_p_and_l}')


    # The greatest increase in profits (date and amount) over the entire period
    max_delta = (max(profit_loss_delta))
    max_delta_mo = dates[profit_loss_delta.index(max_delta) + 1]
    print(f'\nGreatest Increase in Profits: {max_delta_mo} ({max_delta})')

    # The greatest decrease in profits (date and amount) over the entire period
    min_delta = (min(profit_loss_delta))
    min_delta_mo = dates[profit_loss_delta.index(min_delta) + 1]
    print(f'\nGreatest Decrease in Profits: {min_delta_mo} ({min_delta})')

financial_analysis(file_name)
