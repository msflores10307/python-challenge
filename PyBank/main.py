import os
import csv
### CODE NEEDS COMMENTING AND CLEANUP
data_path = os.path.join(".", "Resources", "budget_data.csv")
month_column = []
prof_loss_column = []
changes = []
monthly_prof = {}
with open(data_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)
    row_counter = 0
    for row in csv_reader:
        month_column.append(str(row[0]))
        prof_loss_column.append(float(row[1]))
        monthly_prof.update( {str(row[0]) : [row[1]]} )
        row_counter = row_counter + 1

monthly_changes = {}
for i in range(len(prof_loss_column)-1):
    changes.append(prof_loss_column[i+1]-prof_loss_column[i])
    monthly_changes.update( {month_column[i+1]: prof_loss_column[i+1]-prof_loss_column[i] } ) # shows the change between current month and previous
    # indexes of this matrix are one less than in main month matrix because first month is not included
mini = changes.index(min(changes))
maxi = changes.index(max(changes))

# The total number of months included in the dataset
month_count = len(month_column)
# The net total amount of "Profit/Losses" over the entire period
TotalProfitLoss = sum(prof_loss_column)
# The average of the changes in "Profit/Losses" over the entire period
avg = sum(changes)/len(changes)
# The greatest increase in profits (date and amount) over the entire period
# print(month_column[maxi+1])
# print(monthly_changes[month_column[maxi+1]])
# # The greatest decrease in losses (date and amount) over the entire period
# print(month_column[mini+1])
# print(monthly_changes[month_column[mini+1]])
#print(monthly_changes[mini])


output_string = f'''
Financial Analysis
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Total Months: {month_count}
  Total: ${TotalProfitLoss}
  Average  Change: ${avg}
  Greatest Increase in Profits: {month_column[maxi+1]}(${monthly_changes[month_column[maxi+1]]})
  Greatest Decrease in Profits: {month_column[mini+1]} (${monthly_changes[month_column[mini+1]]})
'''

print(output_string)
output_path = os.path.join(".", "analysis", "output.csv")

with open(output_path, "w") as outfile:
    outfile.write(output_string)

