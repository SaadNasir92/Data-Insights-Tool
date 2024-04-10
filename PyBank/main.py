# PyBank Instructions
# In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. 
# The dataset is composed of two columns: "Date" and "Profit/Losses".

# Your task is to create a Python script that analyzes the records to calculate each of the following values:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period


#1. Read the CSV Data.
import csv
line_num = 0
file_name = 'C:/Users/saad/Documents/SMU Data Science Bootcamp/Mod 3 PYTHON/python-challenge/PyBank/Resources/budget_data.csv'
with open(file_name, 'r') as file:
    raw_data = csv.reader(file)
    data = [line for line in raw_data]

print(data)
# Separate the dates and the p/l in to their own respectives lists.
dates = [row[0] for row in data if row[0]!= 'Date']
profit_and_losses = [int(row[1]) for row in data if row[1]!= 'Profit/Losses']

#2. The total number of months included in the dataset 

total_months = len(dates)



#3. The net total amount of "Profit/Losses" over the entire period

net_total = sum(profit_and_losses)

#4. The changes in "Profit/Losses" over the entire period, and then the average of those changes
def get_change(num1,num2):
    '''Takes 2 numbers, finds the difference and returns the result.
'''
    pass
