import os
import csv

# Read the data from the CSV file
file_path = '/Users/coblehartman/Documents/Berkeley/Module Challenges/module-challenge-three/python-challenge/PyBank/Resources/budget_data.csv'

data = []
with open(file_path, 'r') as file:
    next(file)  # Skip the header
    for line in file:
        line = line.strip().split(',')
        date = line[0]
        profit_loss = int(line[1])
        data.append((date, profit_loss))

# Calculate the total number of months
total_months = len(data)

# Calculate the net total amount of "Profit/Losses"
net_total = sum(row[1] for row in data)

# Calculate the changes in "Profit/Losses" over the entire period
changes = [data[i+1][1] - data[i][1] for i in range(len(data) - 1)]
average_change = sum(changes) / len(changes)

# Find the greatest increase and decrease in profits
max_increase = max(changes)
max_decrease = min(changes)
max_increase_index = changes.index(max_increase) + 1
max_decrease_index = changes.index(max_decrease) + 1

# Retrieve dates for greatest increase and decrease
max_increase_date = data[max_increase_index][0]
max_decrease_date = data[max_decrease_index][0]

analysis_results = [
    "Financial Analysis",
    "-----------------------------",
    f"Total Months: {total_months}",
    f"Total: ${net_total}",
    f"Average Change: ${average_change:.2f}",
    f"Greatest Increase in Profits: {max_increase_date} (${max_increase})",
    f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})"
]

# Print the analysis
for result in analysis_results:
    print(result)

# Export the results to a text file
output_file = '/Users/coblehartman/Documents/Berkeley/Module Challenges/module-challenge-three/python-challenge/PyBank/analysis/financial_analysis.txt'
with open(output_file, 'w') as file:
    for result in analysis_results:
        file.write(result + "\n")

print(f"Analysis has been exported to {output_file}")