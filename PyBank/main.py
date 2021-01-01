import os
import csv

path = os.path.join('..', 'Resources', 'budget_data.csv')

with open(path) as budget:

    csvreader = csv.reader(budget, delimiter=',')

    print('Financial Analysis') 
    print('------------------------------------')
    
    next(csvreader)
    
    total_month = 0
    net_total = 0
    change_profit = []
    counter = 0
    min_profit = 0
    max_profit = 0
    max_change_date = ''
    min_change_date = ''

    for row in csvreader:
        total_month += 1 
        
        net_total  += int(row[1])
        if counter != 0:
            change_profit.append(int(row[1]) - previous_row)
            
            if (int(row[1]) - previous_row) >  max_profit:
                max_profit = (int(row[1]) - previous_row)
                max_change_date = row[0]

            if (int(row[1]) - previous_row) <  min_profit:
                min_profit = (int(row[1]) - previous_row)
                min_change_date = row[0]
            
        previous_row = int(row[1])
        counter += 1



    print("Total Months: ", str(total_month))
    print("Total: $", str(net_total))
    print("Average Change: $", str(round(sum(change_profit)/len(change_profit),2)))
    print("Greatest Increase in Profits: ", max_change_date, "$ ", max(change_profit))
    print("Greatest Decrease in Profits: ", min_change_date, "$ " , min(change_profit))


output_file = os.path.join('..', 'analysis', 'analysis.txt')


with open(output_file, "w", newline='') as txt_file:
    txt_file.write('Financial Analysis')
    txt_file.write('\n')
    txt_file.write('------------------------------------')
    txt_file.write("\n")
    txt_file.write("Total Months: " + str(total_month))
    txt_file.write("\n")
    txt_file.write("Total: $" + str(net_total))
    txt_file.write("\n")
    txt_file.write("Average Change: $" + str(round(sum(change_profit)/len(change_profit),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase in Profits: " + max_change_date + "$ " + str(max(change_profit)))
    txt_file.write("\n")
    txt_file.write("Greatest Decrease in Profits: " + min_change_date + "$ " + str(min(change_profit)))


