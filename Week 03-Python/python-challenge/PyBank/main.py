import csv

import os

csvpath = os.path.join('..', 'budget_data.csv')


diff = 0

Date = [] 
Price = []  
Profit = [] 
Average_profit = [] 

total_months = 0

total = 0
previous = 0
count = 0

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        
        total += int(row[1])

 #add title
        Date.append(row[0])

# #add Amount
        Price.append(int(row[1]))

# # #Total months
        diff = int(row[1]) - previous
        previous = int(row[1])
        Profit.append(diff)



total_months = len(Date)

#Average change

average_change = (Price[-1] - Price[0])/(len(Price)-1)

#greatest Increase in Profit and Greatest Decrease in Profit
increase = max(Profit)

decrease = min(Profit)

month_dec = 0
month_inc = 0

print(f'Financial Analysis')
print(f'___________________________')
print(f'Total Months: {total_months}')
print(f'Total: ${total}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {month_inc} ({increase})')
print(f'Greatest Decrease in Profits: {month_dec} ({decrease})')



#Final Step: Print the analysis, export a .txt file with results

with open('PyBank.txt', 'w') as text_file:
    print(f'Financial Analysis', file=text_file)
    print(f'___________________________', file=text_file)
    print(f'Total Months: {total_months}', file=text_file)
    print(f'Total: ${total}', file=text_file)
    print(f'Average Change: ${average_change:.2f}', file=text_file)
    print(f'Greatest Increase in Profits: {month_inc} ({increase})', file=text_file)
    print(f'Greatest Decrease in Profits: {month_dec} ({decrease})', file=text_file)












