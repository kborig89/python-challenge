import os
import csv

csvpath=os.path.join('..','homework','python_homework''budget_data.csv')

date=[]
profit_loses=[]
monthly_change=[]

with open(udemy_csv,encoding='utf-8') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    for row in csvreader:
    csv_header=next(csvreader)
        date.append(row[0])
        profit_loses.append(int(row[1]))


print("Finacial Analysis")
print("----------------------")
print("Total Months =..."+str(len(date)))

net_total=sum(profit_loses)
print("Total=..." + net_total)

i in range((profit_loses)-1):
    monthly_change.append(profit_loses[i+1]-profit_loses[i])

maxprofit=max(monthly_change)
minprofit=min(monthly_change)
average={round(sum(monthly_change/len(monthly_change),2))}
print("Average Change =..."+str(average))
print("Greatest Increase in profits =..."+ str(maxprofit))
print("Greatest Decrease in profits = ..."+str(minprofit))


exit()
output_file=os.path.join("budget_data_complete")
with open(file_to_output,"w") as txt_file:
    txt_file.write(output)
