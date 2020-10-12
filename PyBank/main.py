# Task is to create a Python script that analyzes the records to calculate each of the following:
# Import dependencies
import os
import csv

# Create file path to csv file
budget_csv = os.path.join('../Resources/budget_data.csv')
analysis_file = os.path.join('../Analysis/budget_analysis.txt')

# Lists/variables to store data in 
total_months = 0
change_month = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999]
total_net = 0

# with open as csvfile:

with open(budget_csv) as budget_data:
    reader = csv.reader(budget_data)
    header = next(reader)
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:
        # Track total number of months and total profit/loss
        total_months += 1
        total_net += int(row[1])
        # Track net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        change_month += [row[0]]
        # Add profit_loss for month
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

average_change = sum(net_change_list) / len(net_change_list)

# Output summary
output = (
    f"Financial Analysis\n"
    f"*********************\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Incresae in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")


print(output)

with open(analysis_file, "w") as txt_file:
    txt_file.write(output)