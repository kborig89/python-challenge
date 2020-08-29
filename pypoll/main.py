import os
import csv

csvpath=os.path.join('resources','election_data.csv')

voter_id=[]
county=[]
candidate=[]
khan_count=0
li_count=0
correy_count=0
otooley_count=0
vote_count=0


with open(csvpath,encoding='utf-8') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

        if row[2]=="Khan":
            khan_count +=1
        elif row[2] == "Li":
            li_count +=1
        elif row[2] == "Correy":
            correy_count +=1
        else:
            otooley_count +=1


print("Election Results")
print("------------------------")
print("Total Votes =" + str(len(voter_id)))
print('---------------------------')


candidate=["Khan","Li","Correy","Otooley"]
vote_count=[khan_count,li_count,correy_count,otooley_count]

candidate_vote_count=zip(candidate,vote_count)

khan_percent=round(khan_count/(len(voter_id)),3)*100
li_percent=round(li_count/(len(voter_id)),3)*100
correy_percent=round(correy_count/(len(voter_id)),3)*100
otooley_percent=round(otooley_count/(len(voter_id)),3)*100
winner=(max(vote_count))

print(f'Khan:{khan_percent}% ({khan_count})')
print(f'li:{li_percent}% ({li_count})')
print(f'correy:{correy_percent}% ({correy_count})')
print(f'otooley:{otooley_percent}% ({otooley_count})')
print('---------------------------')
print(f'Winner: {winner}')
print('---------------------------')







