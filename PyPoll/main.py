#PyBank Challenge

#Import Modules

import os
import csv

#Define Variables
months = []
profitlosschange =[]

count_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0

#Set path for cvs file
#csvpath = os.path.join("..", "Resources", "budget_data.csv")
csvpath = os.path.join("Homeworks/03-Python/Instructions/PyBank/Resources/budget_data.csv")

#Open and read csv file
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    #Read Header Row
    csv_header=next(csvfile)

    #Start looping through the file

for row in csv_reader:
    #count the months
    count_months += 1
    
    #Net total amount of "Profit/Losses" over the entire period
    current_month_profit_loss = int(row[1])
    net_profit_loss += current_month_profit_loss

    if (count_months ==1):
        previous_month_profit_loss = current_month_profit_loss

    else:
        profit_loss_change = current_month_profit_loss - previous_month_profit_loss
        
        #Add Date
        months.append(row[0])

        profit_loss_change.append(profit_loss_change)
        previous_month_profit_loss = current_month_profit_loss

    #Sum average of the changes
    sum_profit_loss = sum(profit_loss_change)
    average_profit_loss = round(sum_profit_loss/(count_months - 1),2)

    #Highest and Lowest Changes in profit
    highest_change = max(profit_loss_change)
    lowest_change = min(profit_loss_change)

    #Value of highest and lowest changes in "profit/losses" over the entire period
    highest_month_index = profit_loss_change.index(highest_change)
    lowest_month_index = profit_loss_change.index(lowest_change)

    #Assigning Best and worst month
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

    #Print anylysis

    print("Financial Analysis")
    print("------------------------")
    print(f"Total Months: {count_months}")
    print(f"Total: ${net_profit_loss}")
    print(f"Average Change: ${average_profit_loss}")
    print(f"Greatest Increase in profits: {best_month} (${highest_change})")
    print(f"Greatest Decrease in Losses: {worst_month} (${lowest_change})")
