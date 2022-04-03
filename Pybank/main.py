#PyBank Challenge

#Import Modules
import os
import csv

#Define Variables
# months = []
# profitlosschange =[]
month_count = []
profit = []
change_profit = []
# previous_month_profit_loss = 0
# current_month_profit_loss = 0
# profit_loss_change = 0

#Set path for cvs file
#csvpath = os.path.join("..", "Resources", "budget_data.csv")
csvpath = os.path.join("Resources/budget_data.csv")

#Open and read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
 

    #Start looping through the file
    for row in csvreader:
    #count the months
        month_count.append(row[0])
        profit.append(int(row[1]))
    for x in range(len(profit)-1):
        change_profit.append(profit[x+1]-profit[x])

#Evaluate the max and min from the list made
increase = max(change_profit)
decrease = min(change_profit)

#Use the index
month_increase = change_profit.index(max(change_profit))+1
month_decrease = change_profit.index(min(change_profit))+1

# print(net_profit_loss)
         # arr= []
         # if (count_months ==1):
         #     previous_month_profit_loss = current_month_profit_loss

         # else:
         #     profit_loss_change = current_month_profit_loss - previous_month_profit_loss
         #     previous_month_profit_loss = current_month_profit_loss
         #     print(profit_loss_change)
         #     arr.append(int(profit_loss_change))
         # print(len(arr))



     # #Sum average of the changes
     # sum_profit_loss = sum(profit_loss_change)
     # average_profit_loss = round(sum_profit_loss/(count_months - 1),2)
     # print(average_profit_loss)

     # #Highest and Lowest Changes in profit
     # highest_change = max(profit_loss_change)
     # lowest_change = min(profit_loss_change)

     # #Value of highest and lowest changes in "profit/losses" over the entire period
     # highest_month_index = profit_loss_change.index(highest_change)
     # lowest_month_index = profit_loss_change.index(lowest_change)



    # #Print anylysis

print("Financial Analysis")
print("------------------------")
print(f"Total Months: {len(month_count)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
print(f"Greatest Increase in profits: {month_count[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in profits: {month_count[month_decrease]} (${(str(decrease))})")


output = os.path.join("analysis", 'financialanalysis.txt')
with open(output, "w") as new_analysis:
    new_analysis.write(f"```")
    new_analysis.write("\n")
    new_analysis.write("Financial Analysis")
    new_analysis.write("\n")
    new_analysis.write("-------------------")
    new_analysis.write("\n")
    new_analysis.write(f"Total Months: {len(month_count)}")
    new_analysis.write("\n")
    new_analysis.write(f"Total: ${sum(profit)}")
    new_analysis.write("\n")
    new_analysis.write(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
    new_analysis.write("\n")
    new_analysis.write(f"Greatest Increase in profits: {month_count[month_increase]} (${(str(increase))})")
    new_analysis.write("\n")
    new_analysis.write(f"Greatest Decrease in profits: {month_count[month_decrease]} (${(str(decrease))})")
    new_analysis.write("\n")
    new_analysis.write(f"```")