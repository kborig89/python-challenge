import os
import csv

csvpath=os.path.join('resources','budget_data.csv')

date=[]
profit_loses=[]
monthly_change=[]
total_months=0
net_total=0
previous_net=0

with open(csvpath,encoding='utf-8') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)
    firstrow=next(csvreader)
    date.append(firstrow[0])
    profit_loses.append(int(firstrow[1]))
    previous_net=int(firstrow[1])
    for row in csvreader:
        date.append(row[0])
        profit_loses.append(int(row[1]))
        net_change=int(row[1])-previous_net
        previous_net=int(row[1])
        monthly_change.append(net_change)

print("Finacial Analysis")
print("----------------------")
print("Total Months ="+str(len(date)))

net_total=sum(profit_loses)
print(f"Total=: {net_total}")


maxprofit=max(monthly_change)
maxindex= monthly_change.index(maxprofit)
maxdate=date[maxindex+1]
minprofit=min(monthly_change)
minindex=monthly_change.index(minprofit)
mindate=date[minindex+1]
average=round(sum(monthly_change)/len(monthly_change),2)
print("Average Change ="+str(average))
print(f"Greatest Increase in profits: {maxdate}(${maxprofit})")
print(f"Greatest Decrease in profits: {mindate}(${minprofit})")


output_file=os.path.join("budget_data_complete")
with open(file_to_output,"w") as txt_file:
    txt_file.write(output)
