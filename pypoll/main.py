import os
import csv

csvpath=os.path.join('..','homework','python_homework''election_data.csv')
voter_id[]
county[]
candidate[]

print("Election Results")
print("------------------------")

with open(udemy_csv,encoding='utf-8') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    for row in csvreader:
    csv_header=next(csvreader)
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])


print("Total Votes =..."+str(len(voter_id)))


exit()
output_file = os.path.join("budget_data_complete")
 with open(file_to_output, "w") as txt_file:
    txt_file.write(output)