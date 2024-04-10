#1. Read the CSV Data.
import csv
file_name = 'PyBank/Resources/budget_data.csv'
with open(file_name, 'r') as file:
    raw_data = csv.reader(file)
    data = [line for line in raw_data]

# Separate the dates and the p/l in to their own respectives lists.
dates = [row[0] for row in data if row[0]!= 'Date']
profit_and_losses = [int(row[1]) for row in data if row[1]!= 'Profit/Losses']

#2. The total number of months included in the dataset 

total_months = len(dates)



#3. The net total amount of "Profit/Losses" over the entire period

net_total = sum(profit_and_losses)

#4. The changes in "Profit/Losses" over the entire period, and then the average of those changes

profit_loss_delta = [(profit_and_losses[index+1] - profit_and_losses[index]) for index in range(len(profit_and_losses)) if profit_and_losses[-1] != profit_and_losses[index]]

average_p_and_l = round(sum(profit_loss_delta)/len(profit_loss_delta), 2)

#5. The greatest increase in profits (date and amount) over the entire period
#debugging line to compare len of delta vector vs the initial vector.
# print(len(profit_loss_delta))
max_delta = (max(profit_loss_delta))
max_delta_mo = dates[profit_loss_delta.index(max_delta) + 1]


#6. The greatest decrease in profits (date and amount) over the entire period
min_delta = (min(profit_loss_delta))
min_delta_mo = dates[profit_loss_delta.index(min_delta) + 1]

